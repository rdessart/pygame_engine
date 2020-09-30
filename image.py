# !/usr/bin/python3
# coding : utf-8

"""Image loading and display"""

import logging as log
import os

import pygame
# from pygame import locals


class Image():
    """Image"""
    def __init__(self,):
        """Constuctor"""
        self._image = None
        self._image_rect = None

    def load_from_file(self, path: str, color_key=None) -> bool:
        """Load image from a file"""
        fullpath = os.path.join(__file__, path)
        try:
            image = pygame.image.load(fullpath)
        except pygame.error as exception:
            log.warning("Unable to load image from %s\n%s"
                        % (fullpath, exception))
            return False
        self._image = image.convert()
        if color_key is not None:
            if color_key is -1:
                color_key = self._image.get_at((0, 0))
            self._image.set_colorkey(color_key)
            self._image_rect = self._image.get_rect()
        return True

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._image_rect
