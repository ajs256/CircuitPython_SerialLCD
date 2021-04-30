Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-serial-lcd/badge/?version=latest
    :target: https://circuitpython-serial-lcd.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://github.com/ajs256/CircuitPython_SerialLCD/workflows/Build%20CI/badge.svg
    :target: https://github.com/ajs256/CircuitPython_SerialLCD/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black
.. image:: https://img.shields.io/badge/maintained-sporadically-green
    :alt: Maintained sporadically

CircuitPython helper library for Parallax's serial LCDs


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-seriallcd/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-seriallcd

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-seriallcd

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-seriallcd

Usage Example
=============

.. code-block:: python

    import seriallcd
    import busio
    import board

    uart = busio.UART(board.TX, None, baudrate=9600)

    disp = seriallcd.Display(uart) # Create the display object, passing in the UART.

    disp.set_backlight(True) # Turn on the backlight.
    disp.print("Hello CircuitPython!") # Add some text to the display

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/ajs256/CircuitPython_SerialLCD/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
