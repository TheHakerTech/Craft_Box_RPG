from rich.tree import Tree
from rich.console import Console

console = Console()

total_loc_name = None
def set_map(location, total_loc_name):
    _map = Tree("[bold green]Карта")
    rec_walk_locs(location, _map)
    return _map

class Location:
    def __init__(
        self, name: str, entities: dict, hardlevel: int, description, underlocs=dict()
    ):
        """
        Busic class for locations. Parameters:
        -`name` str location name
        -`hardlevel` int location hardlevel
        -`description` location description
        All parameters are requared
        """
        self.name = name.lower()
        self.underlocs = underlocs
        self.entities = entities

        self.ent_names = {str(k): v for (k, v) in enumerate(self.entities.values(), 1)}
        self.names = {str(k): v for (k, v) in enumerate(self.underlocs.values(), 1)}

        self.hardlevel = hardlevel
        self.description = description

    def doc(self):
        return str(self.description)

        
shop = Location(
    "Магазин",
    {},
    2,
    "Магазин полезных вещей",
)
tram = Location(
    "Трамвай", {}, 1, "Трамвайная дорога проложенная с давних времён..."
)
tram_station = Location(
    "Трамвайная станция", {}, 3, "", underlocs={tram.name: tram}
)

the_crossroads = Location(
    "Перепутье",
    {},
    1,
    "Подземная дорога что ведёт в глубины королевства...",
    underlocs={shop.name: shop, tram_station.name: tram_station},
)

def rec_walk_locs(location, map_):
    global total_loc_name
    if   location.hardlevel == 1:
        b_map = map_.add(f"[bold green]{location.name.title()}")
    elif location.hardlevel == 2:
        b_map = map_.add(f"[bold yellow]{location.name.title()}")
    elif location.hardlevel == 3:
        b_map = map_.add(f"[bold red]{location.name.title()}")
    elif location.hardlevel == 4:
        b_map = map_.add(f"[bold puple]{location.name.title()}")
    if location.underlocs == {}:
        return None
    else:
        for loc in location.underlocs.values():
            rec_walk_locs(loc, b_map)

s = set_map(the_crossroads, shop.name)
console.print(s)