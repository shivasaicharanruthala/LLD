from abc import ABC, abstractmethod


"""
1. A Null object replaces NULL value.
2. No need to put if check for checking NULL.
3. Null object reflects doNothing or Default behavior.
"""


class Object(ABC):
    @abstractmethod
    def method(self):
        pass


class RealObject(Object):
    def method(self):
        return True


class NullObject(Object):
    def method(self):
        return False


def NewObject(obj) -> Object:
    if obj:
        return RealObject()
    return NullObject()


if __name__ == '__main__':
    print(NewObject(False).method())
