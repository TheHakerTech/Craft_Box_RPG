from rich.tree import Tree
from rich.console import Console

console = Console()

total_loc_name = None


def set_map(location, total_loc_name):
    _map = Tree("[bold green]Карта")
    rec_walk_locs(location, _map)
    return _map


def rec_walk_locs(location, map_):
    global total_loc_name
    if location.hardlevel == 1:
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
