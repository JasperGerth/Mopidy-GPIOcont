****************************
Mopidy-GPIOcont
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-GPIOcont.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-GPIOcont/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/jaspergerth/mopidy-gpiocont/master.svg?style=flat
    :target: https://travis-ci.org/jaspergerth/mopidy-gpiocont
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/jaspergerth/mopidy-gpiocont/master.svg?style=flat
   :target: https://coveralls.io/r/jaspergerth/mopidy-gpiocont
   :alt: Test coverage

This is an extension for Mopidy to control your music via buttons. There are 4 dedicated playlist buttons, when pressed
a playlist starts. Volume control is done via a rotary encoder and the LCD screen displays relevant information.


Installation
============

Install by running::

    pip install Mopidy-GPIOcont

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-GPIOcont to your Mopidy configuration file (~./etc/mopidy/mopidy.conf). Note that the list_name are strings and should not be followed by a space. ::

    [gpiocont]
    enabled = true
    play_pin = 4
    next_pin = 23
    prev_pin = 24
    vol_a_pin = 17
    vol_b_pin = 18
    vol_bounce_time = 10
    vol_change = 2
    list1_pin = 6
    list2_pin = 13
    list3_pin = 19
    list4_pin = 26
    list1_name = Awesome Mix Vol.1
    list2_name = Awesome Mix Vol.2
    list3_name = Heerenhuis UU7
    list4_name = Loge, koffie!
    lcd_enable = true
    lcd_address = 38
    lcd_port = 1

The configuration shown here is also the default configuration. Below is an explanation for each setting
(Pins are in BCM mode you can see `here <http://raspberrypi.stackexchange.com/a/12967>`_  what your pin numbers are.).

Since Mopidy-GPIOcont uses the internal pullup resistors of your Raspberry, buttons should be connected as:

[Pin] -> [Button] -> [Ground].

Configuration options
=====================
Not all config values have to be set, below is an explanation for each configuration value.

REQUIRED

``enabled``: If the extension is enabled or not.

``list<i>_name``: Name of your dedicated playlist (no trailing spaces).

``lcd_address``: Address of your LCD screen on the I2C bus. Hexadecimal without the leading "0x".
Can be found with ``sudo i2cdetect -y 1`` or ``sudo i2cdetect -y 0``.
This command uses the i2c-tools ``sudo apt-get install i2c-tools``.

OPTIONAL (Else default values are used)

``play_pin``: Location of your play/pause button.

``next_pin`` and ``prev_pin`` : Location of your next and previous button.

``vol_a_pin``: Location of channel A of your rotary encoder (also sometimes CLK).

``vol_b_pin``: Location of channel B of your rotary encoder (also sometimes DT).

``list<i>_pin``: Location of your dedicated playlist buttons.

``lcd_enable``: If you want to enable your LCD screen.

``lcd_port``: Port of the I2C bus (0 for RasPi 1 and 1 for Raspi 2/3).


These two settings have to be adjusted to fit your rotary encoder if your volume control is not working well.

``vol_bounce_time``: Time in milliseconds to wait before another edge is detected on channel A.

``vol_change``: Change in volume (up/down) per detected edge on channel A.







Project resources
=================

- `Source code <https://github.com/jaspergerth/mopidy-gpiocont>`_
- `Issue tracker <https://github.com/jaspergerth/mopidy-gpiocont/issues>`_
- `Development branch tarball <https://github.com/jaspergerth/mopidy-gpiocont/archive/master.tar.gz#egg=Mopidy-GPIOcont-dev>`_


Credits
=======

- Original author: `Jasper Gerth <https://github.com/jaspergerth`__
- Current maintainer: `Jasper Gerth <https://github.com/jaspergerth`__
- `Contributors <https://github.com/jaspergerth/mopidy-gpiocont/graphs/contributors>`_


Changelog
=========
v0.2.2 (RELEASED)
----------------------------------------
- Playlists working
- Volume and current track shown on lcd screen
- Volume control working (needs some work)

v0.2.0 (UNRELEASED)
----------------------------------------
- Play/Pause working
- Prev/Next working
- Dedicated playlist pins working
- LCD screen working (Only used on boot)

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.

