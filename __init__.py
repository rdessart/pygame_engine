#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging as log

import pygame


sucess, failure = pygame.init()
if failure > 0:
    log.warning("Caution %d module(s) of pygame failed to start", failure)
else:
    log.debug("Pygame loaded sucessfully")