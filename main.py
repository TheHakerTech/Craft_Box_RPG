# -*- coding: utf-8 -*-
from colors import TColors as c
import libs.entity as entity
from libs.entity import AllEntities
import libs.items as items
from libs.items import AllItems
import libs.location as location

LEN_LINE = 15*3
RPG = f"""
{c.br(c.red("================"))}{c.br(c.blue("==============="))}{c.br(c.yellow("================"))}
{c.br(c.red("=┏━━━━━━━━━━━┓=="))}{c.br(c.blue("=┏━━━━━━━━━━━┓="))}{c.br(c.yellow("=┏━━━━━━━━━━━┓=="))}
{c.br(c.red("=┃===┏━━━━┓==┃=="))}{c.br(c.blue("=┃===┏━━━━━┓ ┃="))}{c.br(c.yellow("=┃===┏━━━━━━━┛=="))}
{c.br(c.red("=┃===┗━━━━┛==┃=="))}{c.br(c.blue("=┃===┗━━━━━┛ ┃="))}{c.br(c.yellow("=┃===┃=========="))}
{c.br(c.red("=┃===━━━━━━┓━┛=="))}{c.br(c.blue("=┃===┏━━━━━━━┛="))}{c.br(c.yellow("=┃===┃ ┏━━━━━┓=="))}
{c.br(c.red("=┃===┏━━━┓ ┗━━┓="))}{c.br(c.blue("=┃===┃========="))}{c.br(c.yellow("=┃===┃ ┗━━━┓ ┃=="))}
{c.br(c.red("=┃===┃===┗━┓==┃="))}{c.br(c.blue("=┃===┃========="))}{c.br(c.yellow("=┃===┗━━━━━┛ ┃=="))}
{c.br(c.red("=┗━━━┛=====┗━━┛="))}{c.br(c.blue("=┗━━━┛========="))}{c.br(c.yellow("=┗━━━━━━━━━━━┛=="))}
{c.br(c.red("================"))}{c.br(c.blue("==============="))}{c.br(c.yellow("================"))}
"""

class Input:
    def __init__(self,
                 text: str,
                 stop=lambda x: x!=x,
                 correct=lambda x: x==x):
        """
        Class for inputing means from console
        Parameters:
        -`text` str text that will be in input
        -`stop` function if it is true while will stop
        -`correct` lambda is cheacking mean before return
        """
        while True:
            self._input = str(input(text)).lower()
            if stop(self._input):
                break
                continue
            elif correct(self._input):
                break
                continue

    def __int__(self):
        return int(self._input)

    def __str__(self):
        return str(self._input)

LOADSAVE = 1
LASTSAVE = 2
NEWSAVE = 3
EXIT = 4

# Make locations
shop = location.Location("Магазин", [AllEntities.moat_npc], 2, "Магазин полезных вещей")
tram = location.Location("Трамвай", [], 0, "Трамвайная дорога проложенная с давних времён...")
tram_station = location.Location("Трамвайная станция", [], 0, "",
    underlocs=[tram])

the_crossroads = location.Location("Перепутье", [], 1, "Подземная дорога что ведёт в глубины королевства...",
    underlocs=[shop, tram_station])
tram.parent = tram_station
tram_station.parent = the_crossroads
shop.parent = the_crossroads

names_dict = location.locations_dict
ent_names_dict = entity.entities_dict


class Game:
    def __init__(self):
        print(RPG)
        self.loading()
        self.main_menu()
        self.choice = str(Input(c.br(c.red("> ")), correct=lambda x: str(x) in ("1","2","3","4")))
        self.save = Save(game=self)

    def main_menu(self):
        print(c.br(c.blue("="*LEN_LINE)))
        print(c.yellow("Привет добро пожаловать в RPG! Загрузи сохранение или создай новое."))
        print(c.br(c.red("1.Загрузить сохранение\n2.Последние сохранение\n3.Новое сохранение\n4.Выход (Ctrl+C)")))

    def loading(self):
        for i in range(16):
            print((c.br(c.red("━"))), end="")
        for i in range(15):
            print((c.br(c.blue("━"))), end="")
        for i in range(16):
            print((c.br(c.yellow("━"))), end="")
        print("\n")

class Player(entity.PlayableEntity):
    def __init__(self, xp: float, damage: float,
                 name: str, armors: list or tuple,
                 weapons: list or tuple, items,
                 description, block_damage):
        # Init params
        self.xp           = xp
        self.damage       = damage
        self.name         = name
        self.armors       = armors
        self.description  = description
        self.items        = items
        # Reinit params with changes
        self.block_damage = 0
        for armor in self.armors:
            self.block_damage = self.block_damage + armor.block_damage

        print(self.description)

    def doc(self):
        return str(self.description)

class Save(AllItems):
    def __init__(self, game: Game):
        self.game = game
        self.total_location = the_crossroads
        if int(self.game.choice) == LOADSAVE:
            pass
        elif int(self.game.choice) == LASTSAVE:
            pass
        elif int(self.game.choice) == NEWSAVE:
            self.player = Player(xp=10.0,
                                 damage=0.1,
                                 name="Рыцарь",
                                 armors=[self.busic_shell],
                                 weapons=[self.old_sword],
                                 description="Рыцарь, не помнящий ничего...",
                                 block_damage=0.2,
                                 items=(self.old_sword, self.cape, self.busic_shell))
            while True:
                # Выводим меню
                self.menu() 
                if self.choice == "1": # Вещи
                    self.inventory() # Открыть инвентарь
                elif self.choice == "2": # Локации
                    self.show_locations()
                elif self.choice == "3":
                    pass
                elif self.choice == "4":
                    pass
                else:
                    if str(self.choice).lower() in self.total_location.names:
                        self.total_location = names_dict[str(self.choice).lower()]
                        self.show_locations()

                    elif str(self.choice).lower() in self.total_location.ent_names:

                        if ent_names_dict[str(self.choice).lower()].identifier == entity.EntType.NPC:
                            ent_names_dict[str(self.choice).lower()].start_dialog()
                        elif ent_names_dict[str(self.choice).lower()].identifier == entity.EntType.BOSS:
                            ent_names_dict[str(self.choice).lower()].start_dialog()
                            print("Сразится с {0} [y/n]".format(ent_names_dict[str(self.choice).lower()].name))
                            answer = str
                        self.show_locations()


                    if str(self.choice).lower() == self.total_location.parent.name:
                        self.total_location = self.total_location.parent
                        self.show_locations()
            
        elif int(self.game.choice) == EXIT:
            raise KeyboardInterrupt

    def show_locations(self):
        # Если есть подлокации
        if self.total_location.underlocs != list() or self.total_location.underlocs != tuple():
            # Показать текущию
            print("Текущая локация: {0}".format(self.total_location.name))
            # Показать подлакации
            print("Подлокации: (<имя_локации> чтобы идти в локацию)")
            for under_loc in self.total_location.underlocs: # Циклом перебераем подлокации
                print("{0}. {1}".format(under_loc.name, under_loc.description))
            print("{0}. (Выход)".format(self.total_location.parent.name))
        else: # Если подлокаций нет
            # Показать текущию
            print("Текущая локация: {0}".format(self.total_location.name))
            # Показать то что подлакаций нет
            print("Подлокации: нету подлокаций (<имя_локации> чтобы идти в локацию)")
        # Вывод существ
        # Проверяем, есть ли существа в текущей локации
        if self.total_location.entities != list() or self.total_location.entities != tuple():
            print("Существа: (<имя_существа> чтобы поговорить\сразится)")
            for ent in self.total_location.entities:
                print("{0}. {1}. {2}".format(ent.name, ent.identifier, ent.description))
            
        else:
            print("Существа: Нет существ (<имя_существа> чтобы поговорить\сразится)")

    def inventory(self):
        print("Вещи")
        for item in self.player.items:
            print("{0}. {1}. {2}".format(c.br(c.red(item.name)), c.br(c.blue(item.description)),
            c.br(c.blue(item.interesting))))

    def menu(self):
        print(c.br(c.red("1.Вещи\n2.Доступные локации\n3.Навыки\n4.Сохранить\n")))
        self.choice = str(Input(c.br(c.red("> ")), correct=lambda x: str(x) in ["1","2","3","4"]+self.total_location.names+
            self.total_location.ent_names+[self.total_location.parent.name])).lower()
while True:
    try:
        game = Game()
    except KeyboardInterrupt:
        print("^C")
        print(c.br(c.red("Вы действительно хотите выйти?[y/n]")))
        is_exit = str(Input(text=c.br(c.red("> ")), correct=lambda x: str(x).lower() in ("y", "n")))
        if is_exit.lower() == "y":
            break
        elif is_exit.lower() == "n":
            continue

