#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Image loading and display"""

import logging as log
import os

import pygame


class Drawable():
    """ Drawable """
    def __init__(self):
        """ default contsturctor """
        self.position = ()
        self.surface = None


class Image(Drawable):
    """Image"""
    def __init__(self,):
        """Constuctor"""
        super().__init__()
        self._image = None
        self._image_rect = None
        self.position = (0, 0)

    def load_from_file(self, path: str, color_key=None) -> bool:
        """Load image from a file"""
        fullpath = os.path.join(os.path.dirname(__file__), path)
        try:
            image = pygame.image.load(path)
        except FileNotFoundError as exception:
            log.warning("Unable to load image from %s\n%s"
                        % (fullpath, exception))
            return False
        self._image = image.convert()
        if color_key is not None:
            if color_key == -1:
                color_key = self._image.get_at((0, 0))
            self._image.set_colorkey(color_key)
        self._image_rect = self._image.get_rect()
        self.surface = self._image
        return True

    @property
    def rect(self):
        return self._image_rect
