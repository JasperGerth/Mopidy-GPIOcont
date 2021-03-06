import pykka
import logging
from time import sleep
logger = logging.getLogger(__name__)

from mopidy import core

try:
    import I2C_LCD_driver
except ImportError:
    logger.error("GPIOcont: could not import I2C bus.")



logger.debug("GPIOcont: Frontend.py called")



class GPIOcont(pykka.ThreadingActor, core.CoreListener):

    def __init__(self, config, core):
        super(GPIOcont, self).__init__()
        self.core = core
        self.conf = config

        from .in_gpio import in_GPIO
        self.IO = in_GPIO(self, config['gpiocont'])
        self.vol_change = config['gpiocont']['vol_change']
        self.lcd_enabled=config['gpiocont']['lcd_enable']

        if self.lcd_enabled:
            #Initialize the LCD display
            try:
                lcd_addr = int(config['gpiocont']['lcd_address'], 16) #Converts the address string (i.e. '0x38') to a hex integer
                lcd_port = config['gpiocont']['lcd_port']

                self.lcd = I2C_LCD_driver.lcd(lcd_addr, lcd_port)
                self.lcd.lcd_display_string("BOOTING", 1)
                self.lcd.lcd_display_string("git: jaspergerth", 2)
                sleep(0.5)
                self.lcd.lcd_clear()
            except IOError:
                logger.error("GPIOcont: Unable to initialize I2C bus, make sure mopidy is in i2c group <sudo adduser mopidy i2c>")

        #Set some tracklist attributes
        self.core.tracklist.set_repeat(True)

    def input_event(self, event):
        #play pause event
        if event['main'] == 'play':
            if self.core.playback.state.get() == \
                    core.PlaybackState.PLAYING:
                self.core.playback.pause()
            else:
                self.core.playback.play()

        #Volume event
        elif event['main'] == 'volume':
            if event['sub'] == 'up':
                curr = self.core.playback.volume.get()
                self.core.playback.volume = curr + self.vol_change
            elif event['sub'] == 'down':
                curr = self.core.playback.volume.get()
                self.core.playback.volume = curr - self.vol_change

        #Playlist event
        elif event['main'] == 'list':
            toPlay = None
            self.core.tracklist.clear()
            for toPlay in self.core.playlists.playlists.get():
                if toPlay.name == event['sub']:
                    break
            for tr in toPlay.tracks:
               self.core.tracklist.add(uri=tr.uri)
            self.core.playback.play()

        #prev/ next event
        elif event['main'] == 'switch':
            if event['sub'] == 'next':
                self.core.playback.next()
            elif event['sub'] == 'prev':
                self.core.playback.previous()


    #Todo implement some stuff that updates the lcd screen.
    #def playback_state_changed(self, old_state, new_state):



    #Todo interrupt current scrolling when new track is played
    def track_playback_started(self, tl_track):
        if self.lcd_enabled:
            empty = " " * 16
            self.lcd.lcd_display_string(empty,1)
            name = tl_track.track.name
            if len(name) <= 16:
                self.lcd.lcd_display_string(name)
            else:
                for i in range(0, len(name)-15):
                    self.lcd.lcd_display_string(empty,1)
                    lcd_text = name[i:(i + 16)]
                    self.lcd.lcd_display_string(lcd_text, 1)
                    sleep(0.2)

                self.lcd.lcd_display_string(name)

    def volume_changed(self, volume):
        if self.lcd_enabled:
            self.lcd.lcd_display_string("VOL",2,10)
            if volume < 100:
                self.lcd.lcd_display_string((' '+str(volume)), 2, 13)
            else:
                self.lcd.lcd_display_string(str(volume), 2, 13)




