# -*- coding: utf-8 -*-


class MagicRaw:
    def __init__(self, count):
        self.count = count
        self.description = str()

    def __doc__(self):
        return str(self.description)


class TheVoid(MagicRaw):
    def __init__(self, count):
        super().__init__(count)
        self.description = """
        Пустота... Странное чёрное вещество... Однако чувствовается знакомое и родное
        """


class TheLight(MagicRaw):
    def __init__(self, count):
        super().__init__(count)
        self.description = """
        Свет... Яркий и неприятный.
        """
