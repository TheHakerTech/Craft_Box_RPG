# -*- coding: utf-8 -*-
import libs.entity as entity
from libs.entity import AllEntities
import libs.items as items
import re
from libs.items import AllItems
import libs.location as location
from saves_manager import *
from rich.console import Console
from libs.magic_raw import *

AllItems = AllItems()


LEN_LINE = 15 * 3
console = Console()
name = "RPG"
TITLE = f"""
{"[bold red] ┏━━━━━━━━━━━┓  "}{"[bold blue] ┏━━━━━━━━━━━┓ "}{"[bold yellow] ┏━━━━━━━━━━━┓  "}
{"[bold red] ┃   ┏━━━━┓  ┃  "}{"[bold blue] ┃   ┏━━━━━┓ ┃ "}{"[bold yellow] ┃   ┏━━━━━━━┛  "}
{"[bold red] ┃   ┗━━━━┛  ┃  "}{"[bold blue] ┃   ┗━━━━━┛ ┃ "}{"[bold yellow] ┃   ┃          "}
{"[bold red] ┃   ━━━━━━┓━┛  "}{"[bold blue] ┃   ┏━━━━━━━┛ "}{"[bold yellow] ┃   ┃ ┏━━━━━┓  "}
{"[bold red] ┃   ┏━━━┓ ┗━━┓ "}{"[bold blue] ┃   ┃         "}{"[bold yellow] ┃   ┃ ┗━━━┓ ┃  "}
{"[bold red] ┃   ┃   ┗━┓  ┃ "}{"[bold blue] ┃   ┃         "}{"[bold yellow] ┃   ┗━━━━━┛ ┃  "}
{"[bold red] ┗━━━┛     ┗━━┛ "}{"[bold blue] ┗━━━┛         "}{"[bold yellow] ┗━━━━━━━━━━━┛  "}
"""


class Input:
    def __init__(self, text: str, stop=lambda x: x != x, correct=lambda x: x == x):
        """
        Class for inputing means from console
        Parameters:
        - `text` str text that will be in input
        - `stop` function if it is true while will stop
        - `correct` lambda is cheacking mean before return
        """
        while True:
            self._input = str(console.input(text))
            if stop(self._input):
                break
            elif correct(self._input):
                break

    def __int__(self):
        return int(self._input)

    def __str__(self):
        return str(self._input)


LOADSAVE = "load"
LASTSAVE = "last"
NEWSAVE = "new"
EXIT = "exit"
INV = "inv"
MAP = "map"
SKILLS = "skills"
LOCS = "locs"
GO = "go"
MAP = "map"
SAVE = "save"
QUIT = "quit"
TALK = "talk"
FIGHT = "fight"

# Make locations
shop = location.Location(
    "Магазин",
    {AllEntities.moat_npc.name: AllEntities.moat_npc},
    2,
    "Магазин полезных вещей",
)
tram = location.Location(
    "Трамвай", {}, 0, "Трамвайная дорога проложенная с давних времён..."
)
tram_station = location.Location(
    "Трамвайная станция", {}, 0, "", underlocs={tram.name: tram}
)

the_crossroads = location.Location(
    "Перепутье",
    {AllEntities.fire_boss.name: AllEntities.fire_boss},
    1,
    "Подземная дорога что ведёт в глубины королевства...",
    underlocs={shop.name: shop, tram_station.name: tram_station},
)
tram.parent = tram_station
tram_station.parent = the_crossroads
shop.parent = the_crossroads

names_dict = location.locations_dict
ent_names_dict = entity.entities_dict

commands1 = ["exit", "help", "new", "last", "load"]
commands2 = [
    "exit",
    "help",
    "skills",
    "inv",
    "map",
    "locs",
    "go",
    "quit",
    "talk",
    "fight",
]

LOCATION = the_crossroads


class Game:
    def __init__(self):
        console.print(TITLE)
        self.main_menu()
        self.choice = str(
            Input("[bold red]> ", correct=lambda x: str(x).lower() in commands1)
        )
        self.save = Save(game=self)

    def main_menu(self):
        console.print("[bold blue]================================================")
        console.print(
            f"[bold green]Привет добро пожаловать в {name}! Загрузи сохранение или создай новое."
        )
        for ch in (
            "[blue]load[/blue] - Загрузить сохранение",
            "[blue]last[/blue] - Последние сохранение",
            " [blue]new[/blue] - Новое сохранение",
            "[blue]exit[/blue] - Выход (Ctrl+C)",
        ):
            console.print(ch)


class Player(entity.PlayableEntity):
    def __init__(
        self,
        xp: float,
        damage: float,
        name: str,
        armors: list or tuple,
        weapons: list or tuple,  # FIXME: never used
        soul_count: TheSoul,
        void_count: TheVoid,
        items: list,
        skills: dict,
        description,
        block_damage,
    ):
        # Init params
        self.xp = xp
        self.full_xp = xp
        self.damage = damage
        self.name = name
        self.armors = armors
        self.weapons = weapons
        self.soul_count = soul_count
        self.void_count = void_count
        self.description = description
        self.skills = skills
        self.items = {k : v for (k, v) in zip(
            [item.name for item in items],
            items
        )}
        print(self.items)

        # Reinit params with changes
        self.block_damage = block_damage
        for armor in self.armors:
            self.block_damage = self.block_damage + armor.block_damage
        

    def __doc__(self):
        return str(self.description)


class Save():
    def __init__(self, game: Game):
        self.game = game
        self.total_location = the_crossroads
        self.pattern = re.compile(r"""[0-9a-zа-яё]+""")
        if self.game.choice == LOADSAVE:
            self = load_game()[0]
            console.print("[bold green]Введите название сохранения")
            self.save_name = str(
                Input(
                    text="[bold red]> ",
                    correct=lambda x: self.pattern.search(str(x).lower()) and not x in saves_list(),
                )
            )
            self.player = self.object_save().player
            self.new_save()
        elif self.game.choice == LASTSAVE:
            pass


        elif self.game.choice == NEWSAVE:
            
            console.print("[bold green]Введите название для сохранения")
            self.save_name = str(
                Input(
                    text="[bold red]> ",
                    correct=lambda x: self.pattern.search(str(x).lower()) and not x in saves_list(),
                )
            )
            
            
            self.player = Player(
                xp=10.0,
                damage=0.1,
                name="Рыцарь",
                armors=[AllItems.busic_shell],
                weapons=[AllItems.old_sword],
                soul_count=TheSoul(0.5),
                void_count=TheVoid(50),
                description="[bold white]Рыцарь, не помнящий ничего...",
                block_damage=0.2,
                skills={"X": (AllItems.old_sword, "Удар гвоздём"),
                "C": (AllItems.basic_shield, "Щит")},
                items=[AllItems.old_sword, AllItems.cape, AllItems.busic_shell, AllItems.basic_shield],
            )
            self.new_save()

        elif self.game.choice == EXIT:
            raise KeyboardInterrupt

    def new_save(self):
        # Modules settings
        items.player = self.player
        console.print(self.player.__doc__())
        save_game(self.save_name, self)
        while True:
            # Выводим меню
            self.menu()
            self.command = self.choice.lower().split(" ")[0]
            correct_command = lambda: len(self.choice.split(" ")) >= 2
            correct_command2 = lambda: len(self.choice.split(" ")) == 1
            if self.command == INV and correct_command2():  # Вещи
                self.inventory()  # Открыть инвентарь
            elif self.command == LOCS and correct_command2():  # Локации
                self.show_locations()  # Показать локации
            elif self.command == SKILLS and correct_command2():
                self.show_skills()
            elif self.command == SAVE and correct_command2():  # Не доделано
                save_game(self.save_name, [self.player, LOCATION])
                console.print("[bold green]Сохранено")
            elif self.command == TALK and correct_command():  # Поговорить
                self.talk()
            elif self.command == FIGHT and correct_command():  # Сразится
                self.fight()
            elif self.command == QUIT and correct_command2():
                if not isinstance(self.total_location.parent, location.BasicLocation):
                    self.total_location = self.total_location.parent
                self.show_locations()
            elif self.command == GO and correct_command():
                self.arg = str(self.choice).lower().split(" ")[1]
                print(self.total_location.names.keys())
                if self.arg in self.total_location.names.keys():
                    self.total_location = names_dict[
                        self.total_location.names[self.arg].name
                    ]
                    self.show_locations()
                else:
                    console.print("[bold red]Введено неверное число")
                    self.show_locations()
            elif self.command == EXIT and correct_command2():
                raise KeyboardInterrupt
    def show_skills(self):
        d = str()
        for skill_name in self.player.skills:
            console.print(
                f"[bold white]{self.player.skills[skill_name][0].name}[/bold white] - [blue]{skill_name}.[/blue] [yellow]{self.player.skills[skill_name][1]}[/yellow]"
            )
            d += f"{skill_name} - {self.player.skills[skill_name][0].name}. {self.player.skills[skill_name][1]},\n"
        return d

    def _exit(self):
        print("^C")
        console.print("[bold red]Вы действительно хотите выйти?[/bold red][y/n]")
        is_exit = str(
            Input(text="[bold red]> ", correct=lambda x: str(x).lower() in ("y", "n"))
        )
        if is_exit.lower() == "y":
            pass

        elif is_exit.lower() == "n":
            pass

    def correct_attack(self, attack: str):
        if len(attack) <= 2:
            result = False
            for n in attack.upper():
                if n in self.player.skills:
                    result = True
                else:
                    result = False
            return result
        else:
            return False


    def fight(self):
        # Задаём переменную `arg`
        self.arg = str(self.choice).lower().split(" ")[1]
        if self.arg in self.total_location.ent_names:
            if (
                self.total_location.ent_names[self.arg].identifier
                == entity.EntType.BOSS
            ):
                enemy = self.total_location.ent_names[self.arg]
                enemy.start_dialog()
                console.print(
                    f"[bold white]Сразится с [bold red]{enemy.name}[/bold red]? [y/n]"
                )
                answer = str(
                    Input(
                        text="[bold red]> ",
                        correct=lambda x: str(x) in ("y", "n"),
                    )
                )
                if answer == "y":
                    console.print(self.show_skills())
                    console.print(
                        f"[bold red]Введите аттаку[/bold red]\n"
                    )
                    while not enemy.xp <= 0:
                        self.attack = str(
                            Input(
                                text="[bold red]> ",
                                correct=lambda x: str(x).upper()
                                in self.player.skills,
                            )
                        ).upper()
                        enemy.update_attack()
                        for atk in self.attack:
                            print(self.player.skills[atk][0])
                            if isinstance(self.player.skills[atk][0], items.Shield):
                                console.print("[bold white]Вы отразили удар")
                            else:
                                if isinstance(enemy.skills[enemy.attack][0], items.Shield):
                                    console.print("[bold white]Противник отразил удар")
                                else:
                                    a = enemy.hit(self.player.skills[atk][0])
                                    b = self.player.hit(enemy.skills[enemy.attack][0])
                                    console.print(
                                        f"Вы нанесли: {a[1]} {round(enemy.xp, 1)}/{round(enemy.full_xp, 1)}"
                                    )
                                    console.print(
                                        f"Вам нанесли: {b[1]} {round(self.player.xp, 1)}/{round(self.player.full_xp, 1)}"
                                    )
                                    if self.player.xp <= 0:
                                        break
                            
                                

                    else:
                        enemy.death_event(enemy.after_death)
                        console.print(
                            f"[bold yellow]Вы победили[/bold yellow] [bold red]{enemy.name}"
                        )
                        console.print(
                            f"[bold white]Вы получили {enemy.drop.name}[/bold white] [bold yellow]{enemy.drop.description}"
                        )
                        enemy.drop.received()
                        self.player.items[enemy.drop.name] = enemy.drop
                        del self.total_location.entities[enemy.name]

    def talk(self):
        # Задаём переменную `arg`
        self.arg = str(self.choice).lower().split(" ")[1]
        if self.arg in self.total_location.ent_names:
            if self.total_location.ent_names[self.arg].identifier == entity.EntType.NPC:
                self.total_location.ent_names[self.arg].start_dialog()

    def show_locations(self):
        # Если есть подлокации
        if (
            self.total_location.underlocs != list()
            or self.total_location.underlocs != tuple()
        ):
            # Показать текущию
            console.print(
                f"[bold green]Текущая локация[/bold green][bold white] {self.total_location.name}"
            )
            # Показать подлокации
            console.print("[bold green]Подлокации[/bold green]")
            self.loc_index = 0
            for num in self.total_location.names: # Циклом перебераем подлокации
                console.print(
                    f"[blue]{num}[/blue][bold white] - {self.total_location.names[num].name}[/bold white] [bold yellow]{self.total_location.names[num].description}[/bold yellow]"
                )
                self.loc_index += 1

            if not isinstance(self.total_location.parent, location.BasicLocation):
                console.print(
                    f"[blue]quit[/blue][bold white] - {self.total_location.parent.name}[/bold white] (Выход)"
                )
        # Вывод существ
        # Проверяем, есть ли существа в текущей локации
        if (
            self.total_location.entities != list()
            or self.total_location.entities != tuple()
        ):
            console.print(f"[bold green]Существа")
            for num, name in enumerate(self.total_location.entities, 1):
                ent = self.total_location.entities[name]
                console.print(
                    f"[blue]{num}[/blue][bold white] - {ent.name}[/bold white] [bold yellow]{ent.description}[/bold yellow]"
                )

    def inventory(self):
        console.print("[bold green]Вещи")
        for item_name in self.player.items:
            console.print(
                f"[bold white]{item_name}[/bold white] [blue]{self.player.items[item_name].description}.[/blue]\
                    [yellow]{self.player.items[item_name].interesting}[/yellow]"
            )

    def menu(self):
        for ch in (
            "   [blue]inv[/blue] - Вещи              (inv)",
            "  [blue]locs[/blue] - Доступные локации (locs)",
            "[blue]skills[/blue] - Навыки            (skills)",
            "  [blue]talk[/blue] - Поговорить        (talk <номер персонажа>)",
            " [blue]fight[/blue] - Сразиться         (fight)",
            "  [blue]save[/blue] - Сохранить         (save)",
            "    [blue]go[/blue] - Переместиться     (go <номер локации>)",
            "  [blue]exit[/blue] - Выход (Ctrl+C)    (выход)",
            "  [blue]quit[/blue] - Выйти назад в предыдущию локацию"
        ):
            console.print(ch)
        self.choice = str(
            Input(
                "[bold red]> ",
                correct=lambda x: str(x).lower().split(" ")[0]
                in commands2
                + [str(ch) for ch in range(1, len(self.total_location.names))],
            )
        ).lower()


if __name__ == "__main__":
    while True:
        try:
            game = Game()
        except KeyboardInterrupt:
            print("^C")
            console.print("[bold red]Вы действительно хотите выйти?[/bold red][y/n]")
            is_exit = str(
                Input(
                    text="[bold red]> ", correct=lambda x: str(x).lower() in ("y", "n")
                )
            )
            if is_exit.lower() == "y":
                break

            elif is_exit.lower() == "n":
                continue
