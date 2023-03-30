from __future__ import annotations
from abc import ABC, abstractmethod

"""
Intent: Action, Transaction

This pattern that turns a request into a stand-alone object that contains all information about the request. 
This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, 
and support undoable operations.

Applicability:
- pattern when you want to parametrize objects with operations
- when you want to queue operations, schedule their execution, or execute them remotely.
- when you want to implement reversible operations.
"""

