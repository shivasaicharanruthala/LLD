from abc import ABC, abstractmethod

"""
Intent:
This pattern that defines the skeleton of an algorithm in the superclass but lets 
subclasses override specific steps of the algorithm without changing its structure.

Applicability:
- let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.
- when you have several classes that contain almost identical algorithms with some minor differences. As a result, 
  you might need to modify all classes when the algorithm changes.
"""


class AbstractClass(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """
    def template_method(self):
        """
        The template method defines the skeleton of an algorithm.
        """
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # These operations already have implementations.

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    # These operations have to be implemented in subclasses.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    """
        Hooks -  Subclasses may override them, but it's not mandatory since the hooks already have default 
        implementation. Hooks provide additional extension points in some crucial places of the algorithm
    """
    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    Concrete classes have to implement all abstract operations of the base
    class. They can also override some operations with a default implementation.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    """
    Usually, concrete classes override only a fraction of base class'
    operations.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    concreteClass1 = ConcreteClass1()
    concreteClass1.template_method()
    print("")

    print("Same client code can work with different subclasses:")
    concreteClass2 = ConcreteClass2()
    concreteClass2.template_method()
