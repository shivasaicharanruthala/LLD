from __future__ import annotations

from DesignUseCases.snake_and_ladder.game import Game

"""
Workflow:

Requirements:
1. Board Size 
    - in general 10 * 10
    - has numbers
    - has Ladder at random cells
    - has snakes at random cells
    - can be dynamically changed at initial setup
2. How many snakes and ladder
    - can be dynamically changed at initial setup
3. how many dices
    - to start with 1 
    - Extension: can have 2 dice in general
4. No of players
5. What is the winning conditions
    - If anyone finish -> games finishes
    - 

Entities:
1. Dice
    - diceCount int  (with this variable we can roll as these many times)
    + RollDice()
2. Jump represent Snake & Ladder  (snake - jump down; ladder - jump up)
    - start int
    - end   int
3. Cells
    - Jump 
4. Board
    - cells [][]Cell (2D array)
    - 
5. Player
    - playerID      int
    - curntPosition int 
6. Game
    - Board
    - Dice
    - Deque for players
    - Player

"""

if __name__ == "__main__":
    newGame = Game(10, 5, 4, 1, 2)
    newGame.Start()

