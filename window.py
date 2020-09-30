# !/usr/bin/python3
# coding : utf-8
import pygame
# from pygame.locals import *


class Window():
    """Handle a graphical windows"""
    def __init__(self, resolution: tuple, do_init: bool = False):
        """Default constructor"""
        if do_init:
            pygame.init()
        self.window = pygame.display.set_mode(resolution)
        self.resolution = resolution
        self.run = True

    def _handle_event(self):
        """handle event in our class"""
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            self.run = False

    def update(self):
        """Update"""

    def draw(self):
        """Draw call"""
        pygame.display.update()

    def game_loop(self):
        while self.run:
            self._handle_event()
            self.update()
            self.draw()
