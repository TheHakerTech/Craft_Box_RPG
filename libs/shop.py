from rich.console import Console

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

    def show(self, money):
        console.print("[bold greed]Магазин:")
        for name, means in self.items:
            console.print(
                f"[bold white]{name} - [/bold white][bold blue]{means[0].description}. \
            {means[0].interesting}[/bold blue][bold green]{means[1]}"
                if money > item[1]
                else f"[bold white]{name} \
             - [/bold white][bold blue]{means[0].description}. {means[0].interesting}[/bold blue][bold red]{means[1]}"
            )

    def buy(self, name):
        console.print(f"[bold white]Куплено: [/bold white]{self.items.pop(name)}")
        self.show()
