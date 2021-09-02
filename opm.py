import timeit

from Board import Board, codeToBoard
from player import Player


def checkValidInput(num):
    """Checks if user has valid input"""
    if isinstance(num, int) and 0 <= num <= 9:
        return True
    else:
        return False


class OnePlayerMode(Board, Player):

    def __init__(self, game, gameSolutionArray):
        """Initialize the one player mode object"""

        super().__init__()

        # Player class
        self._firstPlayer = Player(1)

        # Sudoku game to be player
        self._sudokuGame = game

        # Array of the game solution
        if isinstance(gameSolutionArray, str):
            self._solutionGame = codeToBoard(gameSolutionArray)
        else:
            self._solutionGame = gameSolutionArray

    def play(self):
        """Defines how one player plays the Sudoku game"""

        timingStarts = timeit.default_timer()  # start timer for the player

        while not self._sudokuGame.isFull():
            choice = self.__userMenu()
            if choice == '1':  # fill value

                self.__fillValue()

            elif choice == '2':  # hint
                self.__hintValue()

            elif choice == '3':

                print("      0, 1, 2, 3, 4, 5, 6, 7, 8 ")  # visual representation of the solution
                print("     ---------------------------")
                for row in range(0, self._solutionGame.__len__()):
                    print(row, ": ", self._solutionGame[row])

                self._sudokuGame.sudokuBoard = self._solutionGame

            elif choice == '4':
                exit(9)

            else:
                print("WRONG INPUT FORMAT. TRY AGAIN")
                self.play()

        timingEnds = timeit.default_timer()  # end timer for the player
        self._firstPlayer.setTime(timingEnds - timingStarts)  # calculate time for the player
        self.__gameStat()  # show statistics about player

    def __hintValue(self):
        """Method to provide hint for player when requested"""
        emptyRow, emptyCol = self._sudokuGame.findSpaces()
        print(emptyRow, emptyCol)
        self._sudokuGame.sudokuBoard[emptyRow][emptyCol] = self._solutionGame[emptyRow][emptyCol]  # the solution for the first empty value in the game
        print("HINT:\n"
              "ROW: ", emptyRow, "\n",
              "COL: ", emptyCol, "\n",
              "VALUE: ", self._solutionGame[emptyRow][emptyCol], "\n")
        self._firstPlayer.setPoints(self._firstPlayer.getPoints() - 2)

    def __fillValue(self):
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
                    self._firstPlayer.setPoints(self._firstPlayer.getPoints() + 1)
                else:
                    print("VALUE IS INVALID. SCORE WENT DOWN BY 1")
                    self._firstPlayer.setPoints(self._firstPlayer.getPoints() - 1)

            else:  # not valid input
                print("WRONG INPUT FORMAT. TRY AGAIN")
                self.__fillValue()

        else:  # not valid input
            print("WRONG INPUT FORMAT. TRY AGAIN")
            self.__fillValue()

    def __userMenu(self):
        """displays the user menu"""
        self._sudokuGame.showBoard()
        return input("WHAT OPERATION YOU WISH TO PROCEED:\n"
                     "1 FILL VALUE\n"
                     "2 TAKE A HINT\n"
                     "3 SOLVE THE GAME\n"
                     "4 QUIT THE GAME\n"
                     "(1/2/3: )")

    def __gameStat(self):
        """shows statistics about the player and the game"""
        print("*******************************************\n",
              "Player ID: ", self._firstPlayer.getId(), "\n",
              "Points: ", self._firstPlayer.getPoints(), "\n"
                                                         "Score: ", self._firstPlayer.calculateScore(), "\n")
