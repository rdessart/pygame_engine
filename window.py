# !/usr/bin/python3
# coding : utf-8

import pygame
# from pygame.locals import *

from color import Color


class Window():
    """Handle a graphical windows"""
    def __init__(self, caption: str = "Pygame", do_init: bool = False):
        """Default constructor"""
        if do_init:
            pygame.init()
        self.window = None
        self._resolution = ()
        pygame.display.set_caption(caption)
        self.run = True

    @property
    def resolution(self):
        """Return the current screen resolution"""
        return self._resolution

    @resolution.setter
    def resolution(self, resolution: tuple):
        """Set the size of the screen"""
        self.window = pygame.display.set_mode(resolution,
                                              pygame.HWSURFACE & pygame.SCALED)
        self._resolution = resolution

    @property
    def caption(self):
        """Retrun the caption of the window"""
        return pygame.display.get_caption()[0]

    @caption.setter
    def caption(self, title: str):
        """Set the caption of the window"""
        pygame.display.set_caption(title)

    @property
    def window_size(self):
        """Return the windows size, may be different of of the resolution"""
        return pygame.display.get_window_size()

    @property
    def number_display(self):
        """Return the number of connected display"""
        return pygame.display.get_num_displays()

    def _handle_event(self):
        """handle event in our class"""
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False

    def update(self):
        """Update"""

    def draw(self, clear_color: Color = Color(0, 0, 0)):
        """Draw call"""
        self.window.fill(clear_color.color)
        pygame.display.flip()

    def game_loop(self):
        while self.run:
            self._handle_event()
            self.update()
            self.draw()
