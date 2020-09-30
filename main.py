# !/usr/bin/python3
# coding : utf-8

""" Tutorial zero of my pygame learning"""

from window import Window
from image import Image


def main():
    win = Window()
    win.resolution = (640, 480)
    img = Image()
    img.load_from_file("resources\\image.jpg")
    win.drawables.append(img)
    print(img.rect)
    win.update()
    win.game_loop()


if __name__ == "__main__":
    main()
