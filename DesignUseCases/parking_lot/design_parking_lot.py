from __future__ import annotations

import random
from abc import ABC, abstractmethod
from typing import List
import time
import uuid
from datetime import datetime

"""
Workflow:


Requirements:
1. How many entrances
    - 1 entrance, 1 exit
    - extension: many entrances, many exits
2. Different type of spots
    - 2Wheeler, 4Wheeler
    - extension: Heavy Duty
3. How about parking charges
    - hourly / minutes / Mix
4. Extension: Find nearest parking spot to entrance

Entities:
1. Vehicle
    - vehicleNo
    - type: enum[2Wheeler, 4Wheeler]

2. Ticket
    - entryTime
    - parkingSpot

3. EntranceGate
    - gateNo
    + findParkingSpot
    + bookParkingSpot
    + generateTicket

4. ParkingSpot
    - id
    - type
    - price
    - isEmpty
    - vehicle

5. ExitGate
    - ticket: Ticket
    + totalCost
    + payment
    + updateParkingSpot
"""


class Vehicle:
    vehicleNo: str
    vehicleType: str

    def __init__(self, vehicleNo: str, vehicleType: str):
        self.vehicleNo = vehicleNo
        self.vehicleType = vehicleType


class Ticket:  # has-a Vehicle, ParkingSpot
    uid: int
    entryTime: float
    vehicle: Vehicle
    parkingSpot: ParkingSpot

    def __int__(self):
        self.uid = int(uuid.uuid4())
        self.entryTime = datetime.now().timestamp()

    def printEntryTime(self) -> str:
        date_time = datetime.fromtimestamp(self.entryTime)
        return date_time.strftime("%d-%m-%Y, %H:%M:%S")

    def getEntryTime(self) -> float:
        return self.entryTime

    def setVehicle(self, v: Vehicle):
        self.vehicle = v

    def setParkingSpot(self, ps: ParkingSpot):
        self.parkingSpot = ps


class EntranceGate:
    gateNo: int
    ticket: Ticket
    parkingSpotManager: ParkingSpotManager

    def __init__(self, gateNo:int, psm: ParkingSpotManager = None):
        self.gateNo = gateNo
        self.parkingSpotManager = psm

    def findSpot(self, vehicleType: str, gateNo:int) -> ParkingSpot:
        return self.parkingSpotManager.findAvailableSpots(vehicleType, gateNo)

    def bookSpot(self, v: Vehicle) -> ParkingSpot:
        self.parkingSpotManager.parkVehicle(v)
        pass

    def generateTicket(self, s: ParkingSpot) -> Ticket:
        pass

class ExitGate:
    gateNo: int
    ticket: Ticket
    parkingSpotManager: ParkingSpotManager
    costComputation: CostComputation
    # payment: Payment

    def totalParkingCost(self):
        self.costComputation.priceCalculation(self.ticket)

    def payment(self):
        pass

    def removeVehicle(self):




class CostComputation:
    strategy: PricingStrategy
    ticket: Ticket

    def __init__(self, strategy: PricingStrategy, ticket: Ticket = None):
        self.strategy = strategy
        self.ticket = ticket

    def setTicket(self, ticket: Ticket):
        self.ticket = ticket

    def setPricingStrategy(self, strategy: PricingStrategy):
        self.strategy = strategy

    def priceCalculation(self, ticket: Ticket) -> float:
        return self.strategy.getSpotPrice(ticket)

def CostComputationFactory(vehicleType: str) -> CostComputation:
    if vehicleType == "2W":
        return CostComputation(DefaultPricingStrategy())
    elif vehicleType == "4W":
        return CostComputation(DefaultPricingStrategy())


# class TwoWheelerCostComputation(CostComputation):
#     def __init__(self, strategy: PricingStrategy, ticket: Ticket):
#         super().__init__(strategy, ticket)
#
# class FourWheelerCostComputation(CostComputation):
#     def __init__(self, strategy: PricingStrategy, ticket: Ticket):
#         super().__init__(strategy, ticket)


class PricingStrategy(ABC):
    def calculateParkingTime(self, entryTime: float) -> float:
        parkingTime = datetime.fromtimestamp(datetime.now().timestamp()) - datetime.fromtimestamp(entryTime)
        # hours, remainder = divmod(parkingTime.seconds, 3600)
        # minutes, seconds = divmod(remainder, 60)

        return parkingTime.seconds / 3600

    @abstractmethod
    def getSpotPrice(self, ticket: Ticket) -> float:
        pass


class DefaultPricingStrategy(PricingStrategy):
    def getSpotPrice(self, ticket: Ticket) -> float:
        return ticket.parkingSpot.getSpotPrice() * self.calculateParkingTime(ticket.getEntryTime())



class ParkingSpot:  # has-a Vehicle
    id: int
    type: str
    price: float
    isEmpty: bool
    vehicle: Vehicle | None

    def __init__(self, id):
        self._id = id
        self.isEmpty = True

    def getSpotPrice(self):
        return self.price

    def parkVehicle(self, v: Vehicle):
        self.vehicle = v
        self.isEmpty = False

    def removeVehicle(self):
        self.vehicle = None
        self.isEmpty = True


class TwoWheelerParkingSpot(ParkingSpot):  # is-a ParkingSpot
    def __init__(self, id):
        super().__init__(id)
        self.price = 10

    def getPrice(self) -> int:
        return self.price

    def setPrince(self, price: int):
        self.price = price


class FourWheelerParkingSpot(ParkingSpot): # is-a ParkingSpot
    def __init__(self, id):
        super().__init__(id)
        self.price = 20

    def getPrice(self) -> int:
        return self.price

    def setPrince(self, price: int):
        self.price = price


class ParkingSpotManager(ABC):  # has-a ParkingSpot
    strategy: ParkingStrategy

    def __init__(self, strategy: ParkingStrategy):
        self.strategy = strategy

    def setStrategy(self, strategy: ParkingStrategy):
        self.strategy = strategy

    @abstractmethod
    def findAvailableSpots(self, vehicleType:str, gateNo: int) -> List[ParkingSpot]:
        pass

    @abstractmethod
    def addParkingSpot(self, ps: ParkingSpot):
        pass

    @abstractmethod
    def removeParkingSpot(self):
        pass

    @abstractmethod
    def parkVehicle(self, ps: ParkingSpot, v: Vehicle):
        pass

    @abstractmethod
    def removeVehicle(self, v: Vehicle):
        pass


class TwoWheelerParkingManager(ParkingSpotManager):  # is-a ParkingSpotManager
    parkingSpots: List[ParkingSpot]

    def __init__(self, strategy: ParkingStrategy, parkingSpots: List[ParkingSpot]| None = None):
        self.parkingSpots = parkingSpots
        super().__init__(strategy)

    def findAvailableSpots(self, vehicleType: str, gateNo:int) -> List[ParkingSpot]:
        # return [spot if spot.isEmpty and spot.type == vehicleType else ]
        # use parking strategy to decide on single spot from all possible available spots.
        availableSpots: List[ParkingSpot] = []

        for spot in self.parkingSpots:
            if spot.isEmpty and spot.type == vehicleType:
                availableSpots.append(spot)

        return availableSpots


class FourWheelerParkingManager(ParkingSpotManager):  # is-a ParkingSpotManager
    parkingSpots: List[ParkingSpot]

    def __init__(self, strategy: ParkingStrategy, parkingSpots: List[ParkingSpot]| None = None):
        self.parkingSpots = parkingSpots
        super().__init__(strategy)

    def findAvailableSpots(self, vehicleType: str, gateNo:int) -> List[ParkingSpot]:
        # return [spot if spot.isEmpty and spot.type == vehicleType else ]
        # use parking strategy to decide on single spot from all possible available spots.
        availableSpots: List[ParkingSpot] = []

        for spot in self.parkingSpots:
            if spot.isEmpty and spot.type == vehicleType:
                availableSpots.append(spot)

        return availableSpots

def ParkingManagerFactory(vehicleType: str) -> ParkingSpotManager:
    if vehicleType == "2W":
        return TwoWheelerParkingManager(DefaultParkingStrategy())
    elif vehicleType == "4W":
        return FourWheelerParkingManager(DefaultParkingStrategy())

class ParkingStrategy(ABC):
    @abstractmethod
    def FindParkingSpot(self, entrance: int) -> List[ParkingSpot]:
        pass


class NearToEntrance(ParkingStrategy):
    def FindParkingSpot(self, entrance: int) -> List[ParkingSpot]:
        pass


class NearToElevator(ParkingStrategy):
    def FindParkingSpot(self, entrance: int) -> List[ParkingSpot]:
        pass


class DefaultParkingStrategy(ParkingStrategy):
    def FindParkingSpot(self, entrance: int) -> List[ParkingSpot]:
        pass



if __name__ == "__main__":


