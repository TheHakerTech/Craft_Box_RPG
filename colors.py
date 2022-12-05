# -*- coding: utf-8 -*-
import colorama
from colorama import Fore, Back, Style
"""
Модуль цветов. Используй документацию класса TColors
"""
colorama.init()
class TColors:
    """
    Класс для цветов
    Используйте TColors.red(<текст>) для получения красного текста
    Используйте TColors.redb(<текст>) для получения красного фона
    Список поддерживаемых цветов текста:
    -red
    -blue
    -green
    -black
    -white
    -yellow
    -pink
    Список поддерживаемых цветов фона:
    -redb
    -blueb
    -greenb
    -blackb
    -whiteb
    -yellowb
    -pinkb
    """
    red = lambda text: Fore.RED + str(text) + Style.RESET_ALL
    redb = lambda text: Back.RED + str(text) + Style.RESET_ALL
    blue = lambda text: Fore.BLUE + str(text) + Style.RESET_ALL
    blueb = lambda text: Back.BLUE + str(text) + Style.RESET_ALL
    green = lambda text: Fore.GREEN + str(text) + Style.RESET_ALL
    greenb = lambda text: Back.GREEN + str(text) + Style.RESET_ALL
    black = lambda text: Fore.BLACK + str(text) + Style.RESET_ALL
    blackb = lambda text: Back.BLACK + str(text) + Style.RESET_ALL
    white = lambda text: Fore.WHITE + str(text) + Style.RESET_ALL
    whiteb = lambda text: Back.WHITE + str(text) + Style.RESET_ALL
    yellow = lambda text: Fore.YELLOW + str(text) + Style.RESET_ALL
    yellowb = lambda text: Back.YELLOW + str(text) + Style.RESET_ALL
    pink = lambda text: Fore.PINK + str(text) + Style.RESET_ALL
    pinkb = lambda text: Back.PINK + str(text) + Style.RESET_ALL
    br = lambda text: Style.BRIGHT + str(text) + Style.RESET_ALL