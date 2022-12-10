from __future__ import annotations


class Currency:
    def __init__(
        self,
        num: int,
    ):
        self.name = "гео"
        self.num = num

    def __add__(self, currency: Currency):
        return self.num + currency.num

    def __radd__(self, currency: Currency):
        return currency.num + self.num

    def __sub__(self, currency: Currency):
        return self.num - currency.num

    def __rsub__(self, currency: Currency):
        return currency.num - self.num

    def __int__(self):
        return int(self.num)
