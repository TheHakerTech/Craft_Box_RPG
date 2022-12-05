# -*- coding: utf-8 -*-
"""
Module with class for location - Location
"""
locations_dict = {}


class BasicLocation:
    def __init__(self):
        """
        Busic class for locations. Parameters:
        -`name` str location name
        -`hardlevel` int location hardlevel
        -`description` location description
        All parameters are requared
        """
        self.name = "basic"


class Location:
    def __init__(
        self,
        name: str,
        entities: list or tuple,
        hardlevel: int,
        description,
        underlocs=list(),
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
        self.names = list()
        self.parent = BasicLocation()
        self.entities = entities
        for under_loc in self.underlocs:
            self.names.append(under_loc.name.lower())
        self.ent_names = list()
        for ent in self.entities:
            self.ent_names.append(ent.name.lower())

        self.hardlevel = hardlevel
        self.description = description
        locations_dict[self.name.lower()] = self

    def doc(self):
        return str(self.description)
