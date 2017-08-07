try:
 import RPi.GPIO as GPIO
except ImportError:
    print("Cannot import RPi.GPIO")
from time import sleep

try:
    import I2C_LCD_driver
except ImportError:
    print("Cannot import I2C_driver")

screen = I2C_LCD_driver.lcd(0x38, 1)


class gpiotest():

    def __init__(self):
        #Set bouncetime
        deb_time = 50 #for normal pushbuttons
        vol_deb_time = 10 #for the voluem rotary encoder

        self.pins={}
        self.pins['play_pin'] = 4
        self.pins['vol_A_pin'] = 17
        self.pins['vol_B_pin'] = 18

        #Set pin mode.
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pins['play_pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pins['play_pin'], GPIO.FALLING, callback=self.play, bouncetime=deb_time)

        GPIO.setup(self.pins['vol_A_pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pins['vol_B_pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pins['vol_A_pin'], GPIO.BOTH, callback=self.volume, bouncetime=vol_deb_time)

        print ("Init done.")
        while True:

            sleep(0.5)
            screen.lcd_display_string("77777777777777777s", 1)
            screen.lcd_display_string("HAHAHAA PENIS",2)
            sleep(1)
            screen.lcd_clear()




    def play(self,channel):
        print("Play button pressed")

    def volume(self,channel):
        print("Volume event.")
        if GPIO.input(channel)==1: #it was a rising edge
            if GPIO.input(self.pins['vol_B_pin']) == 0: #clockwise movement
                print ("Volume up!")
            else: #counterclockwise movemnt
                print ("Volume down")

        else: # it was a falling edge.
            if GPIO.input(self.pins['vol_B_pin']) == 1: #clockwise movement
                print ("volume up")
            else: #counterclockwise movement
                print ("Volume down")

print("calling that shizzle")
gpiotest()






