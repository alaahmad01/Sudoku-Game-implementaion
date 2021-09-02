# Alaa Ahmed 1183339
# Final course project

# import necessary libraries
from Board import Board
from opm import OnePlayerMode
from tpm import TwoPlayerMode


def fileToArray(filename):
    """takes file name as an input and returns its data in an array, or returns -1 if it wasn't found"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            array = [inputPreparation(row) for row in lines]
            return array
    except FileNotFoundError:
        print("FILE NOT FOUND\n")
        return -1


#
def inputPreparation(row):
    """Prepares each row of the data array by appending blank values to incomplete lines and converting blank values to '0'"""
    splatted = row.rstrip().split(",")
    if splatted.__len__() < 9:
        for i in range(splatted.__len__(), 9):
            splatted.append('0')
    for index in range(splatted.__len__()):
        if splatted[index] == '':
            splatted[index] = '0'
        if splatted[index].isnumeric():
            splatted[index] = int(splatted[index])
    return splatted


def inputValidation(row):
    """Validates each row of the data by making sure it has 9 integers. accepts strings and returns boolean"""
    if row.__len__() != 9:
        return False
    for index in range(row.__len__()):
        if not isinstance(row[index], int):
            return False
    return True


def modeSelect(Sudoku, sudokuSolutionArray):
    """Allows the user to choose the mode of playing in the Sudoku game. Accepts the Sudoku object and the Sudoku solution"""

    playingMode = input("CHOOSE THE MODE OF PLAYING\n1 ONE PLAYER\n2 TWO PLAYERS\n(1/2): ")

    if playingMode == '1':
        player = OnePlayerMode(Sudoku, sudokuSolutionArray)
        player.play()

    elif playingMode == '2':
        players = TwoPlayerMode(Sudoku, sudokuSolutionArray)
        players.play()

    else:
        modeSelect(Sudoku, sudokuSolutionArray)


def mainGame(Sudoku):
    """Allows the user to select where the Sudoku game will be generated"""
    while True:

        choice = input("WELCOME TO SUDOKU !!\n"
                       "HOW DO YOU WANT TO PLAY THE GAME?\n"
                       "1. RANDOM PLAY\n"
                       "2. FILE PREPARED PLAY\n"
                       "3. QUIT\n"
                       "YOUR CHOICE: (1/2/3)\n")

        if choice == '1':
            boardArray, boardSolved = Sudoku.generateQuestionBoardCode(
                int(input(
                    "CHOOSE LEVEL OF DIFFICULTY:\n0 EASY\n1 MEDIUM\n2 HARD\n(0/1/2): ")))  # generate random Sudoku with certain difficulty level

        elif choice == '2':

            boardArray = fileToArray(input("ENTER THE FILE NAME\n"))

            if boardArray != -1:
                if all(inputValidation(row) for row in boardArray):
                    Sudoku.sudokuBoard = boardArray  # initialize the object
                    SudokuSolution = Board(Sudoku.boardToCode())
                    if not SudokuSolution.solve():
                        print("THE GAME PROVIDED IS NOT SOLVABLE\n")
                        mainGame(Sudoku)
                    else:  # Sudoku chosen isn't solvable
                        boardSolved = SudokuSolution.sudokuBoard
                        del SudokuSolution
                else:  # validation didn't work out
                    print("FILE'S DATA IS INVALID\n")
                    mainGame(Sudoku)
            else:  # File not found
                print("FILE ERROR\n")
                mainGame(Sudoku)
        elif choice == '3':
            exit(9)

        else:
            print("WRONG INPUT")
            mainGame(Sudoku)

        modeSelect(Sudoku, boardSolved)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """The main function"""
    game = Board()  # start the game object
    mainGame(game)  # start playing the game
