#  player class

class Player:
    _ID = 0
    _turn = False
    _points = 0
    _timeToFinish = 1

    def __init__(self, ID):
        """Initialize the player object"""
        self._ID = ID

    def changeTurn(self):
        """change player's turn"""
        self._turn = not self._turn

    def getPoints(self):
        """get player's points"""
        return self._points

    def setPoints(self, new_score):
        """set player's score"""
        self._points = new_score

    def getId(self):
        """get player's ID"""
        return self._ID

    def getTurn(self):
        """get player's turn"""
        return self._turn

    def getTime(self):
        """get player's time required to finish the puzzle"""
        return self._timeToFinish

    def setTime(self, time):
        """set the player's time required to finish the puzzle"""
        self._timeToFinish = time

    def calculateScore(self):
        """ calculate player's score"""
        _score = self._points / 9 * (3600 / self._timeToFinish)
        if _score == 0:
            return 0
        else:
            return _score
