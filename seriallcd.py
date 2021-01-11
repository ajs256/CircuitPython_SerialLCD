# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 ajs256
#
# SPDX-License-Identifier: MIT
"""
`seriallcd`
================================================================================

CircuitPython helper library for Parallax's serial LCDs


* Author(s): ajs256

Implementation Notes
--------------------

**Hardware:**

* `16x2 Parallax Serial LCD <https://www.parallax.com/product/parallax-2-x-16-serial-lcd-with-piezo-speaker-backlit/>`_
* `20x4 Serial LCD <https://www.parallax.com/product/parallax-4-x-20-serial-lcd-with-piezospeaker-backlit/>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/ajs256/CircuitPython_SerialLCD.git"


def hex_to_bytes(cmd):
    return bytes([cmd])


class Display:
    def __init__(self, uart, *, ignore_bad_baud=False):
        self.display_uart = uart
        try:  # Failsafe if they're using a weird serial object that doesn't have a baud rate object
            if uart.baudrate not in [2400, 9600, 19200] and ignore_bad_baud:
                print(
                    "WARN: Your serial object has a baud rate that the display does not support: ",
                    baud,
                    ". Set ignore_bad_baud to True in the constructor to silence this warning.",
                )
        except AttributeError:
            pass

    # Printing

    def print(self, text):  # Standard printing function.
        buf = bytes(text, "utf-8")
        self.display_uart.write(buf)

    def println(
        self, text
    ):  # Standard printing function, but it adds a newline at the end.
        buf = bytes(text, "utf-8")
        self.display_uart.write(buf)
        self.carriage_return()

    def write(self, data):  # For sending raw data as a byte or bytes.
        self.display_uart.write(data)

    # Cursor manipulation

    def cursor_left(self):
        self.display_uart.write(hex_to_bytes(0x08))

    def cursor_right(self):
        self.display_uart.write(hex_to_bytes(0x09))

    def line_feed(self):
        self.display_uart.write(hex_to_bytes(0x0A))

    def form_feed(self):
        # Must pause 5 ms after use
        self.display_uart.write(hex_to_bytes(0x0C))

    def clear(self):  # A more user-friendly name
        self.form_feed()

    def carriage_return(self):
        self.display_uart.write(hex_to_bytes(0x0D))

    def new_line(self):  # A more user-friendly name
        self.carriage_return()

    # Mode setting

    def set_mode(self, cursor, blink):
        if cursor and blink:
            self.display_uart.write(hex_to_bytes(0x19))
        elif cursor and not blink:
            self.display_uart.write(hex_to_bytes(0x18))
        elif not cursor and blink:
            self.display_uart.write(hex_to_bytes(0x17))
        elif not cursor and not blink:
            self.display_uart.write(hex_to_bytes(0x16))

    def set_backlight(self, light):
        if light:
            self.display_uart.write(hex_to_bytes(0x11))
        else:
            self.display_uart.write(hex_to_bytes(0x12))

    # Move to a specific position

    def move_cursor(self, row, col):
        cmd = hex_to_bytes(0x80 + (row * 0x14 + col))
        self.display_uart.write(cmd)

    # TODO: Custom characters

    # TODO: Music functionality
