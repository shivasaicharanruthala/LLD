# Intent: lets you define a subscription mechanism to notify multiple objects about any events that happen to the
# object they’re observing.

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

""" Subject interface  """


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


"""
    Observer should be able to access the state of the subject and Subject must be able to keep track of list of 
    observers subscribed to it. 
"""


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def do_some_business_logic(self):
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observerA = ConcreteObserverA()
    subject.attach(observerA)

    observerB = ConcreteObserverB()
    subject.attach(observerB)

    subject.do_some_business_logic()
    subject.do_some_business_logic()
