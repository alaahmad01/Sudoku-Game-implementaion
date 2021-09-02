import timeit

from Board import Board, codeToBoard
from player import Player


def checkValidInput(num):
    """Checks if user has valid input"""
    if isinstance(num, int) and 0 <= num <= 9:
        return True
    else:
        return False


class TwoPlayerMode(Board, Player):

    def __init__(self, game, gameSolutionArray):
        """Initialize the two player mode object"""
        super().__init__()

        # Player class 1

        self._firstPlayer = Player(1)
        self._secondPlayer = Player(2)

        # Sudoku game to be player
        self._sudokuGame = game

        # Array of the game solution
        if isinstance(gameSolutionArray, str):
            self._solutionGame = codeToBoard(gameSolutionArray)
        else:
            self._solutionGame = gameSolutionArray

        # used to calculate how many times a player requested a pass
        self.passTrack2 = []
        self.passTrack1 = []

    def play(self):
        """defines how two players play the game"""
        while not self._sudokuGame.isFull():
            _timingStarts = timeit.default_timer()  # starting player timer
            _player = self.__findWhoseTurn()  # find which players turn
            print("Player ", _player.getId(), " is playing")
            choice = self.__userMenu()
            self.passTracking(_player, choice)
            if choice == '1':  # fill value

                self.__fillValue(_player)
                self.__switchTurns()

            elif choice == '2':  # pass value
                self.__switchTurns()

                if self.validityForHint():  # checks for validity of hint
                    self.__hintValue()

                _player.setPoints(_player.getPoints() - 1)

            elif choice == '3':
                print("      0, 1, 2, 3, 4, 5, 6, 7, 8 ")
                print("     ---------------------------")
                for row in range(0, self._solutionGame.__len__()):
                    print(row, ": ", self._solutionGame[row])

                self._sudokuGame.sudokuBoard = self._solutionGame
                self.__switchTurns()

            elif choice == '4':
                exit(99)

            else:
                print("WRONG INPUT FORMAT. TRY AGAIN")
                self.play()

            _timingEnds = timeit.default_timer()  # ending player timers

            _player.setTime(_player.getTime() + _timingEnds - _timingStarts)  # calculating player timers

        # calculating player's score
        self.__gameStat(self._firstPlayer)
        if self._firstPlayer.getPoints() >= 0:
            print("Score: ", self._firstPlayer.getPoints() / 9 * (
                    self._firstPlayer.getTime() + self._secondPlayer.getTime() / self._firstPlayer.getTime()), "\n")
        else:
            print("Score: 0")

        self.__gameStat(self._secondPlayer)
        if self._firstPlayer.getPoints() >= 0:
            print("Score: ", self._secondPlayer.getPoints() / 9 * (
                    self._secondPlayer.getTime() + self._firstPlayer.getTime() / self._secondPlayer.getTime()),
                  "\n")
        else:
            print("Score: 0")

    def __switchTurns(self):
        """Swtiches players turns after each round"""
        self._firstPlayer.changeTurn()
        self._secondPlayer.changeTurn()

    def __userMenu(self):
        """Shows the user main menu"""
        self._sudokuGame.showBoard()
        return input("WHAT OPERATION YOU WISH TO PROCEED:\n"
                     "1 FILL VALUE\n"
                     "2 PASS YOUR TURN\n"
                     "3 SOLVE THE GAME\n"
                     "4 QUIT THE GAME\n"
                     "(1/2/3: )")

    def __findWhoseTurn(self):
        """returns a reference to the player whose turn is now"""
        if self._firstPlayer.getTurn():
            return self._firstPlayer
        elif self._secondPlayer.getTurn():
            return self._secondPlayer
        elif self._secondPlayer.getTurn() and self._firstPlayer.getTurn():  # if both turns are valid, return the second player and set the first to false
            self._secondPlayer.changeTurn()
            return self._firstPlayer
        else:  # if both turns are invalid, return the first player and set the second to false
            self._firstPlayer.changeTurn()
            return self._firstPlayer

    def __fillValue(self, player):
        """Fill value in Sudoku's board"""
        self._sudokuGame.showBoard()
        userInput = input("ENTER ROW NUMBER, COLUMN NUMBER AND THE WANTED VALUE SEPARATED IN COMMAS\n"
                          "(ROW,COL,VALUE): ").split(",")
        if userInput.__len__() == 3:
            row = int(userInput[0])
            col = int(userInput[1])
            num = int(userInput[2])

            if checkValidInput(row) and checkValidInput(col) and checkValidInput(num):

                if self._sudokuGame.addValueToBoard(num, (row, col)):
                    print("VALUE IS ADDED. SCORE WENT UP BY 1")
                    player.setPoints(player.getPoints() + 1)
                else:
                    print("VALUE IS INVALID. SCORE WENT DOWN BY 1")
                    player.setPoints(player.getPoints() - 1)

            else:
                print("WRONG INPUT FORMAT. TRY AGAIN")
                self.__fillValue(player)

        else:
            print("WRONG INPUT FORMAT. TRY AGAIN")
            self.__fillValue(player)

    def __hintValue(self):
        """Method to provide hint for player when needed"""
        emptyRow, emptyCol = self._sudokuGame.findSpaces()
        print(emptyRow, emptyCol)
        self._sudokuGame.sudokuBoard[emptyRow][emptyCol] = self._solutionGame[emptyRow][emptyCol]
        print("HINT:\n"
              "ROW: ", emptyRow, "\n",
              "COL: ", emptyCol, "\n",
              "VALUE: ", self._solutionGame[emptyRow][emptyCol], "\n")
        self._firstPlayer.setPoints(self._firstPlayer.getPoints() - 2)

    def __gameStat(self, statFor):
        """shows statistics about the player and the game"""
        print("*******************************************\n",
              "Player ID: ", statFor.getId(), "\n",
              "Points: ", statFor.getPoints(), "\n")

    def passTracking(self, Gamer, func):
        """does pass tracking. When each player plays, this function tracks if the player requested a pass of a fill"""
        if func == '1':
            if Gamer.getId() == 1:
                self.passTrack1.append(0)
            elif Gamer.getId() == 2:
                self.passTrack2.append(0)

        elif func == '2':
            if Gamer.getId() == 1:
                self.passTrack1.append(1)
            elif Gamer.getId() == 2:
                self.passTrack2.append(1)

    def validityForHint(self):
        """If both players passed turns two times, this validates for a hint need instead of another pass"""
        if self.passTrack1[-2:] == [1, 1] and self.passTrack2[-2:] == [1, 1]:
            return True
        else:
            return False
