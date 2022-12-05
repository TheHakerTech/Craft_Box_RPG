# -*- coding: utf-8 -*-
import random

"""
Module items is using for make items
Classes:
-`Weapon`
-`Armor`
"""


class Weapon:
    def __init__(
        self, name: str, damage: float, description, controle="", interesting=""
    ):
        self.name = name
        self.damage = damage
        self.description = description
        self.controle = controle
        self.interesting = interesting

    def doc(self):
        return str(self.description)


class _Armor:
    def __init__(self, name: str, block_damage: float, description, interesting=""):
        self.name = name
        self.block_damage = block_damage
        self.description = description
        self.interesting = interesting


class Armor(_Armor):
    def __init__(self, name: str, block_damage: float, description, interesting=""):
        self.name = name
        self.block_damage = block_damage
        self.description = description
        self.interesting = interesting

    def doc(self):
        return str(self.description)

    def __add__(self, armor):
        return self.block_damage + armor.block_damage

    def __radd__(self, armor):
        return armor.block_damage + self.block_damage


class Shield:
    def __init__(
        self, name: str, lb_block_chance, description, controle="", interesting=""
    ):
        self.name = name
        self.block = None
        self.description = description
        self.controle = controle
        self.interesting = interesting
        self.lb_block_chance = lb_block_chance
        if self.lb_block_chance():
            self.block = True
        else:
            self.block = False

    def update_shield(self):
        if self.lb_block_chance():
            self.block = True
        else:
            self.block = False

    def doc(self):
        return str(self.description)

    def __add__(self, armor: _Armor):
        return self.block_damage + armor.block_damage

    def __radd__(self, armor: _Armor):
        return armor.block_damage + self.block_damage


class Item:
    def __init__(self, name: str, description, interesting=""):
        self.name = name
        self.interesting = interesting
        self.description = description


# Set items
class AllItems:
    ### Weapons
    # Middle
    old_sword = Weapon(
        "Старый гвоздь",
        1.0,
        "Гвоздь, притупившийся в битвах",
        interesting="На рукоятке странный узор...",
    )
    spike = Weapon("Шип", 2.5, "Очень острый")
    the_blade = Weapon("Клинок", 3.0, "Хорош в битвах")
    # Strong
    steel_plate = Weapon("Кинжалы", 3.1, "Они идеальны...")
    the_poisoned_dagger = Weapon(
        "Отравленный кинжал", 3.3, "Позволяет отравить противника"
    )
    bloody_sword = Weapon(
        "Кровавый гвоздь",
        3.5,
        "Неужели это...",
        interesting="На этом мече кровь босса...",
    )
    # More Strong
    nail_pick = Weapon("Гвоздевая пика", 3.7, "Длинное копьё, бьёт на смерть")
    striking_nail = Weapon(
        "Разящий гвоздь", 4.0, "Длинный увесистый гвоздь. Разит на повал, но медленный"
    )
    the_blockhead = Weapon("Дубина", 4.3, "Дубина - хорошое оружие в ближнем бою")

    ### Armors
    busic_shell = Armor(
        "Панцирь", 0.2, "Плохо сдержавает удары", interesting="Создан природой"
    )

    ### Items
    cape = Item(
        "Накидка", "Кое-как спасает от ветра", interesting="Развивается на ветру"
    )
    basic_shield = Shield(
        "Щит",
        lambda: random.randint(1, 3) == 1,
        "Поношенный и страрый",
        interesting="Идивительно как он выживает после ударов",
    )
