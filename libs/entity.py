# -*- coding: utf-8 -*-
import libs.items as items
import random

entities_dict = {}
"""
Module with class for entity - Entity
"""
class EntType():
    BOSS = "boss"
    NPC = "NPC"



class NoPlayableEntity():
    def __init__(self, name: str, 
                 dialog: list or tuple,
                 identifier: EntType, description):
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


class PlayableEntity():
    def __init__(self, xp: float,
                 dialog: list or tuple,
                 name: str, armors: list or tuple,
                 description, block_damage,
                 skills: list or tuple,
                 shild: items.Shield,
                 identifier: EntType, after_death=None):
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
        self.xp           = xp
        self.name         = name
        self.shild        = shild
        self.skills       = skills
        self.after_death  = after_death
        self.armors       = armors
        self.description  = description
        self.identifier   = identifier
        self.attack       = random.choice(self.skills)
        # Reinit params with changes
        self.block_damage = sum(self.armors)
        entities_dict[self.name.lower()] = self

    def start_dialog(self):
        if self.dialog_index > len(self.dialog):
            for les in self.dialog:
                print(les)
                input()
    


    def death_event(self, after_death):
        if after_death != None:
            for les in after_death:
                print(les)
                input()

    def update_attack(self):
        self.attack = random.choice(self.skills)

    def hit(self, weapon: items.Weapon):
        dmg = True
        if self.attack is items.Shield:
            self.shield.update()
            if self.shield.block:
                pass
            else:
                self.xp -= self.weapon.damage - self.block_damage
                dmg = False
        elif self.attack is items.Weapon:
            return self.attack.damage
        if dmg:
            self.xp -= self.weapon.damage - self.block_damage
        if self.xp <= 0:
            death_event(after_death)



    def doc(self):
        return str(self.description)
        
class AllEntities():
    moat_npc = NoPlayableEntity("Моат", (("О, странник!", "Ищешь ли ты смерти?", "Или же вершить судьбу ты призван?"),),
        EntType.NPC, "Старый рыцарь")