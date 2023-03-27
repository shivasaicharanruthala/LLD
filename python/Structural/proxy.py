""""""
from abc import ABC, abstractmethod

"""
Intent

This pattern lets you provide a substitute or placeholder for another object. A proxy controls the access to the 
original object allowing you to perform something before or after the request gets through the original object.
"""

"""
Applicability

Lazy initialization
Access control 
Caching
Logging
Pre-Processing & Post-Processing of requests
"""


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")


class Proxy(Subject):
    def __init__(self, realSubject: RealSubject):
        self._realSubject = realSubject

    def request(self):
        if self.check_access():
            self._realSubject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    real_subject.request()

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    proxy.request()

