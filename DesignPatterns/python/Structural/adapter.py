from __future__ import annotations
from abc import ABC, abstractmethod

"""
Intent

Pattern that allows objects with incompatible interfaces to collaborate.
"""


class Computer(ABC):
    @abstractmethod
    def InsertIntoLightingPort(self):
        pass


class Client:
    def InsertLightningConnectorIntoComputer(self, computer: Computer):
        print("Client inserts Lightning connector into computer.")
        computer.InsertIntoLightingPort()


class Mac(Computer):
    def InsertIntoLightingPort(self):
        print("Lightning connector is plugged into mac machine.")


class Windows:
    def InsertIntoUSBPort(self):
        print("USB connector is plugged into windows machine.")


class WindowsAdapter(Computer):
    def __init__(self, windowsMachine: Windows):
        self._windowsMachine = windowsMachine

    def InsertIntoLightingPort(self):
        print("Adapter converts Lightning signal to USB.")
        self._windowsMachine.InsertIntoUSBPort()


if __name__ == '__main__':
    client = Client()

    mac = Mac()
    client.InsertLightningConnectorIntoComputer(mac)
    print("================================================================")

    windowsMachine = Windows()
    windowsMachineAdapter = WindowsAdapter(windowsMachine)
    client.InsertLightningConnectorIntoComputer(windowsMachineAdapter)

