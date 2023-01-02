from rich.console import Console
from currency import Currency as c
import items

console = Console()


class Shop:
    def __init__(self, items: dict):
        """
        Using:
        >>> shop = Shop(
            items={Item().name:(Item, Currency())}
        )
        """
        self.items = items

    def show(self, money: c):
        console.print("[bold greed]Магазин:")
        for means in self.items:
            console.print(
                f"[bold white]{means[0].name} - [/bold white][bold blue]{means[0].description}. \
                {means[0].interesting}[/bold blue][bold green]{means[1].num}"
                if money.num > means[1].num
                else f"[bold white]{means[0].name} \
                - [/bold white][bold blue]{means[0].description}. {means[0].interesting}[/bold blue][bold red]{means[1].num}"
            )

    def buy(self, name):
        console.print(f"[bold white]Куплено: [/bold white]{self.items.pop(name)}")
        self.show()


shop = Shop(items={items.AllItems.old_sword.name: (items.AllItems.old_sword, c(20))})
shop.show(c(100))
