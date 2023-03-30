""""""

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