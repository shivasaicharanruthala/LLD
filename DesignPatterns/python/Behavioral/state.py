from __future__ import annotations
from abc import ABC, abstractmethod

""""
Intent

This pattern lets an object alter its behavior when its internal state changes. It appears as if object changed its class

Applicability:
- object that behaves differently depending on its current state, the number of states is enormous, and the state-specific 
  code changes frequently.
- class polluted with massive conditionals that alter how the class behaves according to the current values of the class’s fields.
- lot of duplicate code across similar states and transitions of a condition-based state machine
"""


class Context:
    _state = None

    def __init__(self, state: State):
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    _context = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class ConcreteStateA(State):

    def handle1(self):
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self._context.transition_to(ConcreteStateB())

    def handle2(self):
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self):
        print("ConcreteStateB handles request1.")

    def handle2(self):
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self._context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
