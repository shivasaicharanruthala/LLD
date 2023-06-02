import random
from typing import List

from DesignUseCases.snake_and_ladder.cell import Cell
from DesignUseCases.snake_and_ladder.jump import Jump


class Board:
    _cells: List[List[Cell]]

    def __init__(self, boardSize: int, numberOfSnakes: int, numberOfLadders: int):
        self.initializeCells(boardSize)
        self.addSnakesAndLadders(numberOfSnakes, numberOfLadders)

    def getBoardSize(self) -> int:
        return len(self._cells)

    def getCells(self, playerPosition: int) -> Cell:
        row = playerPosition // len(self._cells)
        column = playerPosition % len(self._cells)

        return self._cells[row][column]

    def initializeCells(self, boardSize: int):
        # initialize board with cells of given size
        self._cells = [ [0] * boardSize ] * boardSize

        for i in range(boardSize):
            for j in range(boardSize):
                self._cells[i][j] = Cell()
                self._cells[i][j].jump = None

    def addSnakesAndLadders(self, numberOfSnakes: int, numberOfLadders: int):
        while numberOfSnakes > 0:
            snakeHead = random.randint(1, len(self._cells) * (len(self._cells) - 1))
            snakeTail = random.randint(1, len(self._cells) * (len(self._cells) - 1))

            if snakeTail >= snakeHead:
                continue

            self.getCells(snakeHead).jump = Jump(snakeHead, snakeTail)
            numberOfSnakes -= 1

        while numberOfLadders > 0:
            ladderStart = random.randint(1, len(self._cells) * (len(self._cells) - 1))
            ladderEnd = random.randint(1, len(self._cells) * (len(self._cells) - 1))

            if ladderEnd <= ladderStart:
                continue

            self.getCells(ladderStart).jump = Jump(ladderStart, ladderEnd)
            numberOfLadders -= 1


