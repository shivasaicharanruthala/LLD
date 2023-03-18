from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Reference: https://refactoring.guru/design-patterns/strategy
# Intent: lets you define a family of algorithms,
# put each of them into a separate class, and make their objects interchangeable.

# Strategy is a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable
# inside original context object.

# Delegated the creating different algorithm objects into different class and each class represents one algorithm.
# Context class is class which keeps reference to the algorithm chosen by the client and this can be modified
# at runtime to. It works with all strategies through the same generic interface, which only exposes a single method for
# triggering the algorithm encapsulated within the selected strategy


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List):
        return reversed(sorted(data))


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_business_logic(self):
        res = self._strategy.do_algorithm([9, 3, 5, 1, 7, 6])
        print(res)


if __name__ == "__main__":
    print("Client: Strategy is set to normal sorting.")
    context = Context(ConcreteStrategyA())
    context.do_some_business_logic()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
