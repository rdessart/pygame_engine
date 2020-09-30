# !/usr/bin/python3
# coding : utf-8

""" Tutorial zero of my pygame learning"""

from window import Window


def main():
    Win = Window()
    Win.resolution = (640, 480)
    Win.caption = "Hi"
    print(Win.window_size)
    print(Win.number_display)
    print(Win.caption)
    Win.game_loop()


if __name__ == "__main__":
    main()
