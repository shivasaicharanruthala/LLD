# that lets you ensure that a class has only one instance, while providing a global access point to this instance.

# violating the Single Responsibility Principle, as it solves 2 problem at a time


"""
Steps

1. Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.

2. Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor
   to create an object and saves it in a static field. All following calls to this method return the cached object.
"""

from threading import Lock, Thread


class Singleton:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # This is the only difference
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # The client code.

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("Foo",))
    process2 = Thread(target=test_singleton, args=("Bar",))
    process1.start()
    process2.start()
