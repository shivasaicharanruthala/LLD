"""
Intent: Provides an interface for creating objects in a superclass but
        allows its subclasses to alter the type of object that will be created.
"""

# It allows us to create objects by specifying their common interface at run time without
# imposing their concrete class creation logic.


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Person:
    def __int__(self, fName, lName):
        self._firstName = fName
        self._lastName = lName
        self.accountDetails = None


class BankAccount(ABC):
    @abstractmethod
    def validateUserIdentity(self):
        pass

    @abstractmethod
    def createAccount(self):
        pass


class BusinessAccount(BankAccount):
    def validateUserIdentity(self):
        print("validating user business identity")

    def createAccount(self):
        print("creating business account")


class CheckinAccount(BankAccount):
    def validateUserIdentity(self):
        print("validating user checkin identity")

    def createAccount(self):
        print("creating checkin account")


def NewAccount(accountType) -> BankAccount:
    account: BankAccount = None

    if accountType == "CheckinAccount":
        account = CheckinAccount()
    elif accountType == "BusinessAccount":
        account = BusinessAccount()

    account.validateUserIdentity()
    account.createAccount()

    return account


if __name__ == "__main__":
    NewAccount("CheckinAccount")
