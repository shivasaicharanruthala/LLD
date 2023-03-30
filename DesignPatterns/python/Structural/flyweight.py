import json
from typing import Dict

""""""

"""
Intent: Cache

This pattern lets you fit more objects into available amount of RAM/Space by sharing common data shared by objects and
not keeping all the the data in every object
 
How we do it:
Extrinsic state storage -  create a separate context class that would store the extrinsic state along with reference to 
the flyweight object. This approach would require having just a single array in the container class.

Flyweight and immutability - Since the same flyweight object can be used in different contexts, you have to make sure 
that its state can’t be modified. A flyweight should initialize its state just once, via constructor parameters.
It shouldn’t expose any setters or public fields to other objects.
 
Flyweight factory - For more convenient access to various flyweights, you can create a factory method that manages a 
pool of existing flyweight objects 
Several options where this method could be placed. The most obvious place is a flyweight container. 
Alternatively, you could create a new factory class. Or you could make the factory method static and put it inside an 
actual flyweight class.
"""


class Flyweight:
    """
        The Flyweight stores a common portion of the state (also called intrinsic
        state) that belongs to multiple real business entities. The Flyweight
        accepts the rest of the state (extrinsic state, unique for each entity) via
        its method parameters.
    """

    def __init__(self, shared_state: str):
        self.shared_state = shared_state

    def operation(self, unique_state: str):
        s = json.dumps(self.shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory:
    """
        The Flyweight Factory creates and manages the Flyweight objects. It ensures
        that flyweights are shared correctly. When the client requests a flyweight,
        the factory either returns an existing instance or creates a new one, if it
        doesn't exist yet.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict):
        for state in initial_flyweights:
            # print("initial: ", initial_flyweights)
            # print("here: ", self.get_key(state))
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        """
        Returns a Flyweight's string hash for a given state.
        """

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        Returns an existing Flyweight with a given state or creates a new one.
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        # for k in self._flyweights:
        #     print("state: ", k)
        #     print("shared state: ", self._flyweights[k].shared_state)
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
        factory: FlyweightFactory, plates: str, owner: str, brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # The client code either stores or calculates extrinsic state and passes it
    # to the flyweight's methods.
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()
