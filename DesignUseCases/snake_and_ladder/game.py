from collections import deque

from DesignUseCases.snake_and_ladder.board import Board
from DesignUseCases.snake_and_ladder.dice import Dice
from DesignUseCases.snake_and_ladder.player import Player


class Game:
    _board: Board
    _dice: Dice
    _playersList: deque[Player] = deque([])
    _winner: Player

    def __init__(self, boardSize: int, noOfSnakes: int, noOfLadders: int, noOfDices: int, noOfPlayer: int):
        self._board = Board(boardSize, noOfSnakes, noOfLadders)
        self._dice = Dice(noOfDices)
        self._winner = None
        self._addPlayers(noOfPlayer)

    def _addPlayers(self, noOfPlayers: int):
        for i in range(noOfPlayers):
            player = Player("p" + str(i), 0)
            self._playersList.append(player)

        # player1 = Player("p1", 0)
        # player2 = Player("p2", 0)
        # self._playersList.append(player1)
        # self._playersList.append(player2)

    def Start(self):
        while self._winner is None:
            # check whose turn to play now
            playerToPlay = self._findPlayerTurn()
            print("player turn is: " + playerToPlay.getPlayerID() + " current position is: " + str(
                playerToPlay.getPlayerPosition()))

            # roll the dice
            diceNumber = self._dice.rollDice()
            print("Move by: ", diceNumber)

            # get the new position
            playerNewPosition = playerToPlay.getPlayerPosition() + diceNumber
            playerNewPosition = self._jumpCheck(playerNewPosition)
            playerToPlay.setPosition(playerNewPosition)
            print("player turn is: " + playerToPlay.getPlayerID() + " new position is: " + str(playerNewPosition))

            # check for winning condition
            if playerNewPosition >= self._board.getBoardSize() * self._board.getBoardSize() - 1:
                self._winner = playerToPlay

        print("WINNER IS:" + self._winner.getPlayerID())

    def _findPlayerTurn(self) -> Player:
        playerToPlay = self._playersList.popleft()  # choose 1st player in the deque to play first
        self._playersList.append(playerToPlay)  # add plyer who got chance to play to the last of player list

        return playerToPlay

    def _jumpCheck(self, playerNewPosition: int) -> int:
        if playerNewPosition > self._board.getBoardSize() * self._board.getBoardSize() - 1:
            return playerNewPosition

        cell = self._board.getCells(playerNewPosition)
        if cell.jump is not None and cell.jump.getStart() == playerNewPosition:
            jumpBy = "ladder" if cell.jump.getStart() < cell.jump.getEnd() else "snake"
            print("jump done by: " + jumpBy)

            return cell.jump.getEnd()

        return playerNewPosition
