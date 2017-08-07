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
Mopidy-GPIOcont to your Mopidy configuration file (Note that the list_name are strings and should not be followed by a space)::

    [gpiocont]
    enabled = true
    play_pin = 4
    next_pin = 23
    prev_pin = 24
    vol_a_pin = 17
    vol_b_pin = 18
    list1_pin = 6
    list2_pin = 13
    list3_pin = 19
    list4_pin = 26
    list1_name = 26
    list2_name = 27
    list3_name = 28
    list4_name = 29
    lcd_address = 38
    lcd_port = 1


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

v0.2.0 (UNRELEASED)
----------------------------------------
- Play/Pause working
- Prev/Next working
- Dedicated playlist pins working
- LCD screen working (Only used on boot)

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.

