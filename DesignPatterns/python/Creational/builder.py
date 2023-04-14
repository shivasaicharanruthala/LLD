from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

"""
Intent:

this pattern lets you construct complex objects step-by-step and allows to produce different types & representations of 
an object using same construction code.

Applicability:
- To get rid of a “telescoping constructor”.
- To use same code to be able to create different representations of some product 
"""


class House:
    def __init__(self, b: Builder):
        self._windowType = b._windowType
        self._doorType = b._doorType
        self._floor = b._floor

    def type(self):
        print(f"House of {self._floor} floors is built with {self._windowType} and has a doors of {self._doorType}.")


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @abstractmethod
    def setWindowType(self):
        pass

    @abstractmethod
    def setDoorType(self):
        pass

    @abstractmethod
    def setNumFloor(self):
        pass

    @abstractmethod
    def getHouse(self) -> House:
        pass


class NormalBuilder(Builder):
    def __init__(self):
        self._floor = None
        self._doorType = None
        self._windowType = None

    def setWindowType(self):
        self._windowType = "Wooden Window"

    def setDoorType(self):
        self._doorType = "Wooden Door"

    def setNumFloor(self):
        self._floor = 2

    def getHouse(self) -> House:
        return House(self)


def newNormalBuilder() -> NormalBuilder:
    return NormalBuilder()


class IglooBuilder(Builder):
    def __init__(self):
        self._floor = None
        self._doorType = None
        self._windowType = None

    def setWindowType(self):
        self._windowType = "Snow Window"

    def setDoorType(self):
        self._doorType = "Snow Door"

    def setNumFloor(self):
        self._floor = 1

    def getHouse(self) -> House:
        return House(self)


def newIglooBuilder() -> IglooBuilder:
    return IglooBuilder()


def getBuilder(builderType: str) -> Builder:
    if builderType == "normal":
        return newNormalBuilder()
    elif builderType == "igloo":
        return newIglooBuilder()


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build(self) -> House:
        self._builder.setDoorType()
        self._builder.setWindowType()
        self._builder.setNumFloor()

        return self._builder.getHouse()


if __name__ == "__main__":
    normalBuilder = getBuilder("normal")
    iglooBuilder = getBuilder("igloo")

    director = Director()
    director.builder = normalBuilder

    normalHouse = director.build()
    normalHouse.type()

    director.builder = iglooBuilder
    iglooHouse = director.build()
    iglooHouse.type()
