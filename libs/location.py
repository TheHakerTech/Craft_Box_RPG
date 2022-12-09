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
        entities: dict,
        hardlevel: int,
        description,
        underlocs=dict()
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
        self.parent = BasicLocation()
        self.entities = entities
        
        self.ent_names = {str(k) : v for (k, v) in enumerate(self.entities.values(), 1)}
        self.names = {str(k) : v for (k, v) in enumerate(self.underlocs.values(), 1)}

        self.hardlevel = hardlevel
        self.description = description
        locations_dict[self.name.lower()] = self

    def doc(self):
        return str(self.description)
