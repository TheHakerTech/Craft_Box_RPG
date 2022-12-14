# -*- coding: utf-8 -*-
import libs.items as items
from libs.items import AllItems
import random
from rich.console import Console
from libs.magic_raw import *

AllItems = AllItems()

entities_dict = {}
"""
Module with class for entity - Entity
"""

console = Console()


class EntType:
    BOSS = "boss"
    NPC = "NPC"


class NotPlayableEntity:
    def __init__(
        self,
        name: str,
        dialog: list or tuple,
        identifier: EntType,
        description,
    ):
        self.name = name
        self.dialog = dialog
        self.description = description
        self.identifier = identifier
        self.dialog_index = 0
        entities_dict[self.name.lower()] = self

    def start_dialog(self):
        if self.dialog_index >= len(self.dialog):
            for les in self.dialog[-1]:
                print(les)
                input()
        else:
            for les in self.dialog[self.dialog_index]:
                print(les)
                input()
        self.dialog_index += 1


class PlayableEntity:
    def __init__(
        self,
        xp: float, # хп
        dialog: list or tuple, # Что он говорит. Пример: (([<Фраза1>], [<ФразаN>]),)
        name: str, # Имя
        armors: list or tuple, # Список доспех
        description, # описание
        block_damage, # Дамаг который он блокирует
        skills: list or tuple, # 
        shield: items.Shield, # 
        identifier: EntType, # 
        after_death=None, # 
        every_drop=None, #
        drop=None, # 
    ):
        """
        Busic class for all entities. Parameters:
        -`xp` float entity xp
        -`damage` float entity damage. May be reinforced with using parameter `weapons`
        -`name` str entity name
        -`armors` list or tuple entity armors. They can weaken damage
        -`description` entity description
        -`identifier` entity`s type
        All parameters are requared
        """
        # Init params
        self.xp = xp
        self.full_xp = xp
        self.name = name
        self.shield = shield
        self.skills = skills
        self.after_death = after_death
        self.armors = armors
        self.description = description
        self.identifier = identifier
        self.every_drop = every_drop

        self.block_damage = block_damage
        self.dialog = dialog
        self.attack = None
        self.drop = drop
        # Reinit params with changes
        for armor in self.armors:
            self.block_damage += armor.block_damage
        entities_dict[self.name.lower()] = self

    def start_dialog(self):
        for les in self.dialog[0]:
            print(les)
            input()

    def death_event(self, after_death):
        if after_death != None:
            for les in after_death:
                print(les)
                input()

    def update_attack(self):
        self.attack = random.choice([i for i in self.skills.keys()])

    def hit(self, weapon: items.Weapon):
        self.xp = self.xp + self.block_damage - weapon.damage

        if self.xp <= 0:
            self.death_event(self.after_death)
        return (self.xp, weapon.damage - self.block_damage)

    def doc(self):
        return str(self.description)


class AllEntities:
    moat_npc = NotPlayableEntity(
        "Моат",
        (("О, странник!", "Ищешь ли ты смерти?", "Или же вершить судьбу ты призван?"),),
        EntType.NPC,
        "Старый рыцарь",
    )
    fire_boss = PlayableEntity(
        10.0,
        (
            (
                "О, странник!",
                "Ищешь ли ты смерти?",
                "Или же вершить судьбу ты призван?",
                "Нет",
                "Невозможно",
            ),
        ),
        "Огненный",
        [AllItems.fire_shell],
        "Старый рыцарь",
        0,
        {"X": (AllItems.fire_sword, "Огонь..."),
         "C": (AllItems.basic_shield, "Щит")},
        AllItems.basic_shield,
        EntType.BOSS,
        drop=AllItems.fire_sword,
        every_drop=TheSoul(0.5)
    )
