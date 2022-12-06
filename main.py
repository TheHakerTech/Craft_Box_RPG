# -*- coding: utf-8 -*-
from colors import TColors as c
import libs.entity as entity
from libs.entity import AllEntities
import libs.items as items
from libs.items import AllItems
import libs.location as location
from rich.console import Console
from rich.progress import track
import time

LEN_LINE = 15 * 3
console = Console()
name = "RPG"
RPG = f"""
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
        -`text` str text that will be in input
        -`stop` function if it is true while will stop
        -`correct` lambda is cheacking mean before return
        """
        while True:
            self._input = str(console.input(text))
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
tram = location.Location(
    "Трамвай", [], 0, "Трамвайная дорога проложенная с давних времён..."
)
tram_station = location.Location("Трамвайная станция", [], 0, "", underlocs=[tram])

the_crossroads = location.Location(
    "Перепутье",
    [AllEntities.fire_boss],
    1,
    "Подземная дорога что ведёт в глубины королевства...",
    underlocs=[shop, tram_station],
)
tram.parent = tram_station
tram_station.parent = the_crossroads
shop.parent = the_crossroads

names_dict = location.locations_dict
ent_names_dict = entity.entities_dict


class Game:
    def __init__(self):
        console.print(RPG)
        self.loading()
        self.main_menu()
        self.choice = str(
            Input("[bold red]> ", correct=lambda x: str(x) in ("1", "2", "3", "4"))
        )
        self.save = Save(game=self)

    def main_menu(self):
        console.print("[bold blue]================================================")
        console.print(
            f"[bold green]Привет добро пожаловать в {name}! Загрузи сохранение или создай новое."
        )
        for num, chapter in enumerate(
            [
                "[bold yellow]" + ch
                for ch in (
                    "Загрузить сохранение",
                    "Последние сохранение",
                    "Новое сохранение",
                    "Выход (Ctrl+C)",
                )
            ],
            1,
        ):
            console.print("{0}.{1}".format("[red]" + str(num) + "[/red]", chapter))

    def loading(self):
        """for _ in track(range(100), description='[green]Processing data'):
        time.sleep(0.1)"""
        pass


class Player(entity.PlayableEntity):
    def __init__(
        self,
        xp: float,
        damage: float,
        name: str,
        armors: list or tuple,
        weapons: list or tuple,
        items,
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
        self.description = description
        self.skills = skills
        self.items = items
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
            self.player = Player(
                xp=10.0,
                damage=0.1,
                name="Рыцарь",
                armors=[self.busic_shell],
                weapons=[self.old_sword],
                description="Рыцарь, не помнящий ничего...",
                block_damage=0.2,
                skills={"X":(self.old_sword, "Удар гвоздём")},
                items=[self.old_sword, self.cape, self.busic_shell],
            )
            while True:
                # Выводим меню
                self.menu()
                if self.choice == "1":  # Вещи
                    self.inventory()  # Открыть инвентарь
                elif self.choice == "2":  # Локации
                    self.show_locations()
                elif self.choice == "3":
                    self.show_skills()
                elif self.choice == "4":
                    pass
                else:
                    if str(self.choice).lower() in self.total_location.names:
                        self.total_location = names_dict[str(self.choice).lower()]
                        self.show_locations()

                    elif str(self.choice).lower() in self.total_location.ent_names:

                        if (
                            ent_names_dict[str(self.choice).lower()].identifier
                            == entity.EntType.NPC
                        ):
                            ent_names_dict[str(self.choice).lower()].start_dialog()
                        elif (
                            ent_names_dict[str(self.choice).lower()].identifier
                            == entity.EntType.BOSS
                        ):
                            ent_names_dict[str(self.choice).lower()].start_dialog()
                            console.print(
                                f"Сразится с {ent_names_dict[str(self.choice).lower()].name}? [y/n]"
                            )
                            answer = str(Input(
                                text="[bold red]> ",
                                correct=lambda x: str(x) in ("y","n")
                            ))
                            if answer == "y":
                                enemy = ent_names_dict[str(self.choice).lower()]
                                console.print(f"[bold red]Введите аттаку[/bold red] ({self.show_skills()})\n")
                                while not enemy.xp <= 0:
                                    self.attack = str(Input(
                                        text="[bold red]> ",
                                        correct=lambda x: str(x).upper() in self.player.skills
                                    )).upper()
                                    enemy.update_attack()
                                    a = enemy.hit(self.player.skills[self.attack][0])
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
                                    console.print(f"Вы победили {enemy.name}")
                                    console.print(f"Вы получили {enemy.drop.name} {enemy.drop.description}")
                                    self.player.items.append(enemy.drop)
                    
                                    


                        self.show_locations()

                    if str(self.choice).lower() == self.total_location.parent.name:
                        self.total_location = self.total_location.parent
                        self.show_locations()

        elif int(self.game.choice) == EXIT:
            raise KeyboardInterrupt

    def show_skills(self):
        for skill_name in self.player.skills:
            console.print(f"{skill_name} - {self.player.skills[skill_name][0].name}. {self.player.skills[skill_name][1]}")
            return f"{skill_name} - {self.player.skills[skill_name][0].name}. {self.player.skills[skill_name][1]}\n"



    def show_locations(self):
        # Если есть подлокации
        if (
            self.total_location.underlocs != list()
            or self.total_location.underlocs != tuple()
        ):
            # Показать текущию
            console.print(
                f"[bold yellow]Текущая локация[/bold yellow][red]:[/red] [bold white]{self.total_location.name}"
            )
            # Показать подлокации
            console.print(
                "[bold yellow]Подлокации[/bold yellow][red]:[/red] (<имя_локации> чтобы идти в локацию)"
            )
            for (
                under_loc
            ) in self.total_location.underlocs:  # Циклом перебераем подлокации
                console.print(
                    f"[bold white]{under_loc.name}[/bold white] [bold yellow]{under_loc.description}[/bold yellow]"
                )
            console.print(
                f"[bold white]{self.total_location.parent.name}[/bold white] (Выход)"
            )
        # Вывод существ
        # Проверяем, есть ли существа в текущей локации
        if (
            self.total_location.entities != list()
            or self.total_location.entities != tuple()
        ):
            console.print(f"[bold yellow]Сушества[/bold yellow][red]:[/red]")
            for ent in self.total_location.entities:
                console.print(
                    f"[bold white]{ent.name} {ent.identifier}[/bold white] [bold yellow]{ent.description}[/bold yellow]"
                )

    def inventory(self):
        console.print("[bold red]Вещи")
        for item in self.player.items:
            console.print(
                f"[bold white]{item.name}[/bold white] [blue]{item.description}.[/blue] [yellow]{item.interesting}[/yellow]"
            )

    def menu(self):
        for num, chapter in enumerate(
            [
                "[bold yellow]" + ch
                for ch in (
                    "Вещи",
                    "Доступные локации",
                    "Навыки",
                    "Сохранить",
                    "Выход (Ctrl+C)",
                )
            ],
            1,
        ):
            console.print("{0}.{1}".format("[red]" + str(num) + "[/red]", chapter))

        self.choice = str(
            Input(
                "[bold red]> ",
                correct=lambda x: str(x)
                in ["1", "2", "3", "4"]
                + self.total_location.names
                + self.total_location.ent_names
                + [self.total_location.parent.name],
            )
        ).lower()


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
