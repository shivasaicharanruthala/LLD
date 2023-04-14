from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


"""
Intent:
This pattern lets you copy existing objects without making the code dependent on other classes 

Problem:
1. creating a new object and iterating over all fields to copy each attribute to the new copy of the object is not 
possible because there can be private attributes of the class that cant be copied this way.

2. Need to know the objects class and its members to copy making it dependent on that class.

3. sometimes we only know the interface the object follows but not its concrete class.

Applicability:
1. to reduce the number of subclasses that only differ in the way they initialize their respective objects.
2. when code shouldn’t depend on the concrete classes of objects that you need to copy

"""


class INode(ABC):
    @abstractmethod
    def print(self, indentation: str) -> str:
        pass

    @abstractmethod
    def clone(self) -> INode:
        pass


class File(INode):
    name: str = None

    def __init__(self, filename: str):
        self.name = filename

    def print(self, indentation: str):
        print(indentation + self.name)

    def clone(self) -> INode:
        return File(self.name + "_clone")


class Folder(INode):
    name: str = None
    children: List[INode] = None

    def __init__(self, folderName: str, children: List[INode]):
        self.name = folderName
        self.children = children

    def print(self, indentation: str):
        print(indentation + self.name)
        for file in self.children:
            file.print(indentation + indentation)

    def clone(self) -> INode:
        clonedFolder = Folder(self.name + "_clone", [])

        for file in self.children:
            clonedFolder.children.append(file.clone())

        return clonedFolder


if __name__ == "__main__":
    file1 = File("File1")
    file2 = File("File2")
    file3 = File("File3")

    folder1 = Folder("Folder1", [file1])

    folder2 = Folder("Folder2", [file1, file2, file3])

    print("\nPrinting hierarchy for Folder2")
    folder2.print(" ")

    clonedFolder = folder2.clone()
    print("\nPrinting hierarchy for clone Folder")
    clonedFolder.print(" ")
