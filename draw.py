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

    def set_colorkey(self, color: pygame.Color):
        """Set the alpha color of the surface"""
        self.surface.set_colorkey(color)

    def scale(self, new_res: tuple):
        """ Rescale image to the new resolution"""
        self.surface = pygame.transform.smoothscale(self.surface, new_res)

    def overlay(self, color: tuple, flags=pygame.BLEND_MULT):
        """ Add a color overlay to the surface"""
        self.surface.fill(color, special_flags=flags)


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
                color_key = self._image.get_at((10, 10))
            self._image.set_colorkey(color_key)
        self._image_rect = self._image.get_rect()
        self.surface = self._image
        return True

    def crop(self, width: int, height: int, left: int, top: int):
        self.surface = pygame.Surface([width, height])
        self.surface.blit(self._image, (0, 0), (top, left, width, height))
        self._image_rect = self.surface.get_rect()

    @property
    def rect(self):
        return self._image_rect
