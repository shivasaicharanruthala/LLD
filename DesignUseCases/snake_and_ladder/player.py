class Player:
    _playerID: str
    _curntPosition: int

    def __init__(self, playerID: str, curntPosition: int):
        self._playerID = playerID
        self._curntPosition = curntPosition

    def getPlayerID(self) -> str:
        return self._playerID

    def getPlayerPosition(self) -> int:
        return self._curntPosition

    def setPosition(self, curntPosition: int):
        self._curntPosition = curntPosition
