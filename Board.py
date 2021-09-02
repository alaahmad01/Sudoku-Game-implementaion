import copy
import random


def codeToBoard(code):
    """Static method to convert a string of Sudoku game to a board (array)"""
    board = [[0] * 9 for _ in range(9)]
    for row in range(9):
        for col in range(9):
            board[row][col] = int(code[0])
            code = code[1:]
    return board


class Board:

    def __init__(self, code=None):
        """Initialise the board object"""
        self.__resetBoard()

        if code:  # create a board from the code inputted
            self.code = code

            for row in range(9):
                for col in range(9):
                    self.sudokuBoard[row][col] = int(code[0])
                    code = code[1:]
        else:
            self.code = None

    def boardToCode(self, input_board=None):
        """boardToCode [input_board (optional): list]:
        Convert a board represented by a list into a string representation"""
        if input_board:
            _code = ''.join([str(i) for j in input_board for i in j])
            return _code
        else:
            self.code = ''.join([str(i) for j in self.sudokuBoard for i in j])
            return self.code

    def findSpaces(self):
        """findSpaces []: Finds the first empty space, represented by a 0, on the current board"""
        for row in range(len(self.sudokuBoard)):
            for col in range(len(self.sudokuBoard[0])):
                if self.sudokuBoard[row][col] == 0:
                    return row, col

        return False

    def checkSpace(self, num, space):
        """checkSpace [num: integer, space: tuple]: Returns a bool, depending if the number passed in can exist in a space on the current board, provided by the tuple argument"""
        if not self.sudokuBoard[space[0]][space[1]] == 0:  # check to see if space is a number already
            return False

        for col in self.sudokuBoard[space[0]]:  # check to see if number is already in row
            if col == num:
                return False

        for row in range(len(self.sudokuBoard)):  # check to see if number is already in column
            if self.sudokuBoard[row][space[1]] == num:
                return False

        _internalBoxRow = space[0] // 3
        _internalBoxCol = space[1] // 3

        for i in range(3):  # check to see if internal box already has number
            for j in range(3):
                if self.sudokuBoard[i + (_internalBoxRow * 3)][j + (_internalBoxCol * 3)] == num:
                    return False

        return True

    def solve(self):
        """solve []: Solves the current board using backtracking"""
        _spacesAvailable = self.findSpaces()

        if not _spacesAvailable:
            return True
        else:
            row, col = _spacesAvailable

        for n in range(1, 10):
            if self.checkSpace(n, (row, col)):
                self.sudokuBoard[row][col] = n

                if self.solve():
                    return self.sudokuBoard

                self.sudokuBoard[row][col] = 0

        return False

    def solveForCode(self):
        """solveForCode []: Calls the solve method and returns the solved board in a string code format"""
        return self.boardToCode(self.solve())

    def generateQuestionBoardCode(self, difficulty):
        """generateQuestionBoardCode [difficulty: integer]: Calls the generateQuestionBoard method and returns a question board and its solution in code format"""
        self.sudokuBoard, _solution_board = self.generateQuestionBoard(self.__generateRandomCompleteBoard(), difficulty)
        return self.boardToCode(), self.boardToCode(_solution_board)

    def generateQuestionBoard(self, fullBoard, difficulty):
        """generateQuestionBoard [fullBoard: list, difficulty: integer]: Returns a randomly generated question board and the solution to the same board, the difficulty represents the number of number squares removed from the board"""
        self.sudokuBoard = copy.deepcopy(fullBoard)

        if difficulty == 0:
            _squares_to_remove = 48
        elif difficulty == 1:
            _squares_to_remove = 60
        elif difficulty == 2:
            _squares_to_remove = 72
        else:
            return

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(0, 2)
            _rCol = random.randint(0, 2)
            if self.sudokuBoard[_rRow][_rCol] != 0:
                self.sudokuBoard[_rRow][_rCol] = 0
                _counter += 1

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(3, 5)
            _rCol = random.randint(3, 5)
            if self.sudokuBoard[_rRow][_rCol] != 0:
                self.sudokuBoard[_rRow][_rCol] = 0
                _counter += 1

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(6, 8)
            _rCol = random.randint(6, 8)
            if self.sudokuBoard[_rRow][_rCol] != 0:
                self.sudokuBoard[_rRow][_rCol] = 0
                _counter += 1

        _squares_to_remove -= 12
        _counter = 0
        while _counter < _squares_to_remove:
            _row = random.randint(0, 8)
            _col = random.randint(0, 8)

            if self.sudokuBoard[_row][_col] != 0:
                n = self.sudokuBoard[_row][_col]
                self.sudokuBoard[_row][_col] = 0

                if len(self.findNumberOfSolutions()) != 1:
                    self.sudokuBoard[_row][_col] = n
                    continue

                _counter += 1

        return self.sudokuBoard, fullBoard

    def __generateRandomCompleteBoard(self):
        """__generateRandomCompleteBoard []: Returns a full randomly generated board"""

        self.__resetBoard()

        _l = list(range(1, 10))
        for row in range(3):
            for col in range(3):
                _num = random.choice(_l)
                self.sudokuBoard[row][col] = _num
                _l.remove(_num)

        _l = list(range(1, 10))
        for row in range(3, 6):
            for col in range(3, 6):
                _num = random.choice(_l)
                self.sudokuBoard[row][col] = _num
                _l.remove(_num)

        _l = list(range(1, 10))
        for row in range(6, 9):
            for col in range(6, 9):
                _num = random.choice(_l)
                self.sudokuBoard[row][col] = _num
                _l.remove(_num)

        return self.__generateCont()

    def __generateCont(self):
        """__generateCont []: Uses recursion to finish generating a full board, whilst also making sure the board is solvable by calling the solve method"""

        for row in range(len(self.sudokuBoard)):
            for col in range(len(self.sudokuBoard[row])):
                if self.sudokuBoard[row][col] == 0:
                    _num = random.randint(1, 9)

                    if self.checkSpace(_num, (row, col)):
                        self.sudokuBoard[row][col] = _num

                        if self.solve():
                            self.__generateCont()
                            return self.sudokuBoard

                        self.sudokuBoard[row][col] = 0

        return False

    def findNumberOfSolutions(self):
        """findNumberOfSolutions []: Finds the number of solutions to the current board and returns a list of all the solutions in code format"""
        _z = 0
        _list_of_solutions = []

        for row in range(len(self.sudokuBoard)):
            for col in range(len(self.sudokuBoard[row])):
                if self.sudokuBoard[row][col] == 0:
                    _z += 1

        for i in range(1, _z + 1):
            _board_copy = copy.deepcopy(self)

            _row, _col = self.__findSpacesToFindNumberOfSolutions(_board_copy.sudokuBoard, i)
            _board_copy_solution = _board_copy.__solveToFindNumberOfSolutions(_row, _col)

            _list_of_solutions.append(self.boardToCode(input_board=_board_copy_solution))

        return list(set(_list_of_solutions))

    def __findSpacesToFindNumberOfSolutions(self, board, h):
        """__findSpacesToFindNumberOfSolutions [board: list, h: integer]: Finds the first empty space in the board given as the argument, used within the findNumberOfSolutions method"""
        _k = 1
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0:
                    if _k == h:
                        return (row, col)

                    _k += 1

        return False

    # solves the board using recursion, is used within the findNumberOfSolutions method
    def __solveToFindNumberOfSolutions(self, row, col):
        """__solveToFindNumberOfSolutions [row: integer, col: interger]: Solves the current board using recursion by starting at the position determined by the row and col, used within the findNumberOfSolutions method"""
        for n in range(1, 10):
            if self.checkSpace(n, (row, col)):
                self.sudokuBoard[row][col] = n

                if self.solve():
                    return self.sudokuBoard

                self.sudokuBoard[row][col] = 0

        return False

    # resets the board to an empty state
    def __resetBoard(self):
        """__resetBoard []:Resets the current board to an empty state"""
        self.sudokuBoard = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        return self.sudokuBoard

    def isFull(self):
        """checks if there's empty spaces in the board"""
        for row in range(len(self.sudokuBoard)):
            for col in range(len(self.sudokuBoard[row])):
                if self.sudokuBoard[row][col] == 0:
                    return False

        return True

    def addValueToBoard(self, num, space):
        """adds value to the board object"""
        if self.checkSpace(num, space):
            self.sudokuBoard[space[0]][space[1]] = num
            return True
        else:
            return False

    def showBoard(self):
        """prints a visual representation of Sudoku"""
        print("      0, 1, 2, 3, 4, 5, 6, 7, 8 ")
        print("     ---------------------------")
        for row in range(0, self.sudokuBoard.__len__()):
            print(row, ": ", self.sudokuBoard[row])

    def play(self):
        """abstract method to be implemented in different modes classes"""
        raise NotImplementedError("Must choose mod of play")
