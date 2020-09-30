#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Tutorial zero of my pygame learning"""

import pygame_engine.image as image
import pygame_engine.window as window


def main():
    win = window.Window()
    win.resolution = (640, 480)
    img = image.Image()
    img.load_from_file("resources\\image.jpg")
    win.drawables.append(img)
    print(img.rect)
    win.update()
    win.game_loop()


if __name__ == "__main__":
    main()
