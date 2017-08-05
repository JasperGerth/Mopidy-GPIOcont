import RPi.GPIO as GPIO

import logging
logger = logging.getLogger(__name__)
logger.debug("GPIOcont: input_gpio.py called.")

deb_time = 50 #The debounce time for the gpio input

class input_GPIO():
    def __init__(self, frontend, pins):
        self.frontend = frontend

        try:
            # set pin mode to BCM
            GPIO.setmode(GPIO.BCM)

            # Play button
            GPIO.setup(pins['play_pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pins['play_pin'], GPIO.FALLING, callback=self.play, bouncetime=deb_time)

            # Volume up button
            GPIO.setup(pins['vol_up_pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pins['vol_up_pin'], GPIO.FALLING, callback=self.vol_up, bouncetime=deb_time)

            # Volume down button
            GPIO.setup(pins['vol_down_pin'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pins['vol_down_pin'], GPIO.FALLING, callback=self.vol_down, bouncetime=deb_time)

            logger.debug("GPIOcont: pin events added.")
        except RuntimeError:
            logger.error("GPIOcont: Not enough permission to open GPIO")

    def play(self, channel):
        self.frontend.input_event('play')

    def vol_up(self,channel):
        self.frontend.input_event('vol_up')

    def vol_down(self,channel):
        self.frontend.input_event('vol_down')