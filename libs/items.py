# -*- coding: utf-8 -*-
from __future__ import annotations
import random
from libs.magic_raw import *

"""
Module items is using for make items
Classes:
-`Weapon`
-`Armor`
"""
player = None

class Item:
    def __init__(
        self,
        name: str,
        description,
        interesting="",
        received_func=None
    ):
        self.name = name
        self.interesting = interesting
        self.description = description
        self.is_receivced = False
        self.received_func = received_func

    def __doc__(self):
        return self.description

    def received(self):
        if not self.is_receivced:
            self.is_receivced = True
            self.received_func(self)

class Weapon(Item):
    def __init__(
        self,
        name: str,
        damage: float,
        description,
        waste=None,
        controle="",
        interesting="",
        received_func=None
    ):
        super().__init__(name, description, interesting, received_func)
        self.name = name
        self.damage = damage
        self.description = description
        self.waste = waste
        self.controle = controle
        self.interesting = interesting

    def __doc__(self):
        return str(self.description)


class Armor(Item):
    def __init__(
        self,
        name: str,
        block_damage: float,
        description,
        interesting="",
        received_func=None
    ):
        super().__init__(name, description, interesting, received_func)
        self.name = name
        self.block_damage = block_damage
        self.description = description
        self.interesting = interesting

    def doc(self):
        return str(self.description)

    def __add__(self, armor: Armor):
        return self.block_damage + armor.block_damage

    """def __radd__(self, armor: Armor):
        return armor.block_damage + self.block_damage"""


class Shield(Item):
    def __init__(
        self,
        name: str,
        lb_block_chance,
        description,
        controle="",
        interesting="",
        received_func=None
    ):
        super().__init__(name, description, interesting, received_func)
        self.name = name
        self.description = description
        self.controle = controle
        self.interesting = interesting
        self.lb_block_chance = lb_block_chance
        self.update_shield()

    def update_shield(self):
        if self.lb_block_chance():
            self.block = True
        else:
            self.block = False

    def doc(self):
        return str(self.description)

    def __add__(self, armor: Armor):
        return self.block_damage + armor.block_damage

    def __radd__(self, armor: Armor):
        return armor.block_damage + self.block_damage

# Set items
class AllItems:
    def fire_sword_received(self, _self):
        print(player.items.pop(self.old_sword.name))
    # Weapons
    # Middle
    def __init__(self):
        self.old_sword = Weapon(
            "Старый гвоздь",
            1.0,
            "Гвоздь, притупившийся в битвах",
            interesting="На рукоятке странный узор...",
        )
        self.spike = Weapon("Шип", 2.5, "Очень острый")
        self.the_blade = Weapon("Клинок", 3.0, "Хорош в битвах")
        # Strong
        self.steel_plate = Weapon("Кинжалы", 3.1, "Они идеальны...")
        self.the_poisoned_dagger = Weapon(
            "Отравленный кинжал", 3.3, "Позволяет отравить противника"
        )
        self.fire_sword = Weapon("Огненный гвоздь", 0.9, "Поражает врагов огнём...", received_func=self.fire_sword_received)
        self.bloody_sword = Weapon(
            "Кровавый гвоздь",
            3.5,
            "Неужели это...",
            interesting="На этом мече кровь босса...",
        )
        # More Strong
        self.nail_pick = Weapon("Гвоздевая пика", 3.7, "Длинное копьё, бьёт на смерть")
        self.striking_nail = Weapon(
            "Разящий гвоздь", 4.0, "Длинный увесистый гвоздь. Разит на повал, но медленный"
        )
        self.the_blockhead = Weapon("Дубина", 4.3, "Дубина - хорошое оружие в ближнем бою")

        # Armors
        self.busic_shell = Armor(
            "Панцирь", 0.2, "Плохо сдержавает удары", interesting="Создан природой"
        )
        self.fire_shell = Armor("Огненный панцирь", 0, "", interesting="")

        # Items
        self.cape = Item(
            "Накидка", "Кое-как спасает от ветра", interesting="Развивается на ветру"
        )
        self.basic_shield = Shield(
            "Щит",
            lambda: random.randint(1, 3) == 1,
            "Поношенный и страрый",
            interesting="Идивительно как он выживает после ударов",
        )
