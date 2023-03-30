""""""

"""
Intent: 

This patterns lets you split a large class or a set of closely related classes into separate hierarchies—abstraction 
and implementation which can be developed independently of each other

Applicability:
- Bridge if you need to be able to switch implementations at runtime.
- when you need to extend a class in several orthogonal (independent) dimensions.
"""
from abc import ABC, abstractmethod


class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two class hierarchies.
    It maintains a reference to an object of the Implementation hierarchy and
    delegates all the real work to this object.
    """
    def __init__(self, implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """

    print(abstraction.operation(), end="")


"""
Each Concrete Implementation corresponds to a specific platform and implements
the Implementation interface using that platform's API.
"""


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)

    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)




