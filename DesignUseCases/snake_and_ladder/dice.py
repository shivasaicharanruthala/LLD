import random


class Dice:
    _diceCount: int
    _min: int = 1
    _max: int = 6

    def __init__(self, diceCount: int):
        self._diceCount = diceCount

    def rollDice(self) -> int:
        totalSum: int = 0
        diceUsed: int = 0

        while diceUsed < self._diceCount:
            totalSum += random.randint(self._min, self._max)
            diceUsed += 1

        return totalSum
