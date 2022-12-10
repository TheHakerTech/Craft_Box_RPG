# -*- coding: utf-8 -*-
import os

os.system("")  # for windows

"""
Модуль цветов. Используй документацию класса TColors

Принцип: для смена цвета используется ESC-последовательность, которая записывается так:
\033[XXm

\033[0m - сброс цвета
\033[1m - жирный (яркий) шрифт

3x - foreground
4x - background
x = 0 - black
x = 1 - red
x = 2 - green
x = 3 - yellow
x = 4 - blue
x = 5 - magenta
x = 6 - cyan
x = 7 - white
"""
# FIXME: this module is not used anywhere

class TColors:
    """
    Пример использования:
    >>> from colors import TColors
    >>> print(TColors.red('Hello, world!')) # красный текст
    >>> print(TColors.yellowb('Hello, world!')) # желтый фон
    """

    @staticmethod
    def clr(code):
        return f"\033[{code}m"

    @staticmethod
    def wrap(text, code):
        return TColors.clr(code) + str(text) + TColors.clr(0)

    def black(self, text):
        return self.wrap(text, 30)

    def red(self, text):
        return self.wrap(text, 31)

    def blue(self, text):
        return self.wrap(text, 32)

    def green(self, text):
        return self.wrap(text, 33)

    def black(self, text):
        return self.wrap(text, 34)

    def white(self, text):
        return self.wrap(text, 35)

    def yellow(self, text):
        return self.wrap(text, 36)

    def pink(self, text):
        return self.wrap(text, 37)

    def blackb(self, text):
        return self.wrap(text, 0)

    def redb(self, text):
        return self.wrap(text, 1)

    def blueb(self, text):
        return self.wrap(text, 2)

    def greenb(self, text):
        return self.wrap(text, 3)

    def blackb(self, text):
        return self.wrap(text, 4)

    def whiteb(self, text):
        return self.wrap(text, 5)

    def yellowb(self, text):
        return self.wrap(text, 6)

    def pinkb(self, text):
        return self.wrap(text, 7)

    def br(self, text):
        return self.wrap(text, 1)
