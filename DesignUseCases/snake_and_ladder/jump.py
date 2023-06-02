class Jump:
    _start: int
    _end: int

    def __init__(self, startPt: int, endPt: int):
        self._start = startPt
        self._end = endPt

    def getStart(self) -> int:
        return self._start

    def getEnd(self) -> int:
        return self._end
