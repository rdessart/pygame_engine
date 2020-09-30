# !/usr/bin/python3
# coding : utf-8

"""Color"""


class Color():
    """Handle colors"""
    def __init__(self, r: int = 255, g: int = 255, b: int = 255):
        self._red = r
        self._green = g
        self._blue = b

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value: int):
        self._red = value

    @property
    def green(self):
        return self._red

    @green.setter
    def green(self, value: int):
        self._red = value

    @property
    def blue(self):
        return self._red

    @blue.setter
    def blue(self, value: int):
        self._red = value

    @property
    def color(self):
        return (self._red, self._green, self._blue)
