

# not used anymore

'''import copy
import random

# class to represent the game sudoku
# this class is abstract class
# it implements the abstract method: solve
# depending on how the players play the game, the method solve will be overridden.
class Sudoku:
    array = [['' for col in range(9)] for row in range(9)]

    def __init__(self):
        pass

    # Check if the Sudoku is valid or not (solvable)
    def isValidSudoku(self):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board = self.getArray()
        for i in range(9):
            row = {}
            column = {}
            block = {}
            row_cube = 3 * (i // 3)
            column_cube = 3 * (i % 3)
            for j in range(9):
                if board[i][j] != '' and board[i][j] in row:
                    return False
                row[board[i][j]] = 1
                if board[j][i] != '' and board[j][i] in column:
                    return False
                column[board[j][i]] = 1
                rc = row_cube + j // 3
                cc = column_cube + j % 3
                if board[rc][cc] in block and board[rc][cc] != '':
                    return False
                block[board[rc][cc]] = 1
        return True

    # adds blanks if the input row has missing values
    def formatting(self, row):

        formatted = row.rstrip().split(",")
        if formatted.__len__() < 9:
            for i in range(formatted.__len__(), 9):
                formatted.append('')

        return formatted

    # reads the file input
    def read(self, filename):
        with open(filename, "r") as fh:
            lines = fh.readlines()

            self.array = [self.formatting(row) for row in lines]

            print(self.array)

    # finds the number of solutions to a board and returns the list of solutions
    def findNumberOfSolutions(self):
        _z = 0
        _list_of_solutions = []

        for row in range(len(self.array)):
            for col in range(len(self.array[row])):
                if self.array[row][col] == 0:
                    _z += 1

        for i in range(1, _z + 1):
            _board_copy = copy.deepcopy(self)

            _row, _col = self.__findSpacesToFindNumberOfSolutions(_board_copy.array, i)
            _board_copy_solution = _board_copy.__solveToFindNumberOfSolutions(_row, _col)

            _list_of_solutions.append(self.boardToCode(input_board=_board_copy_solution))

        return list(set(_list_of_solutions))


    # generates a question board with a certain number of cells removed depending on the chosen difficulty
    def generateQuestionBoard(self, fullBoard, difficulty):

        self.array = copy.deepcopy(fullBoard)

        if difficulty == 0:
            _squares_to_remove = 36
        elif difficulty == 1:
            _squares_to_remove = 46
        elif difficulty == 2:
            _squares_to_remove = 52
        else:
            return

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(0, 2)
            _rCol = random.randint(0, 2)
            if self.array[_rRow][_rCol] != '':
                self.array[_rRow][_rCol] = ''
                _counter += 1

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(3, 5)
            _rCol = random.randint(3, 5)
            if self.array[_rRow][_rCol] != '':
                self.array[_rRow][_rCol] = ''
                _counter += 1

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(6, 8)
            _rCol = random.randint(6, 8)
            if self.array[_rRow][_rCol] != '':
                self.array[_rRow][_rCol] = ''
                _counter += 1

        _squares_to_remove -= 12
        _counter = 0
        while _counter < _squares_to_remove:
            _row = random.randint(0, 8)
            _col = random.randint(0, 8)

            if self.array[_row][_col] != '':
                n = self.array[_row][_col]
                self.array[_row][_col] = ''

                if len(self.findNumberOfSolutions()) != 1:
                    self.array[_row][_col] = n
                    continue

                _counter += 1

        return self.array, fullBoard

    def check_input_validity(self, user_input):
        row = user_input[0]
        col = user_input[1]
        num = user_input[2]
        grid = self.getArray()

        for x in range(9):
            if grid[row][x] == num.__str__():
                return False

        for x in range(9):
            if grid[x][col] == num.__str__():
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num.__str__():
                    return False
        return True
        pass

    def fill(self):

        user_input = (
            input("Enter the row number"), input("Enter the column Number"),
            input("Enter the value you want to fill with"))

        if self.check_input_validity(user_input):
            return True
        else:
            return False

    def auto_solve(self,row,col):
        grid=self.getArray()
        if row == 9 - 1 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if grid[row][col] != '':
            return self.auto_solve(row, col + 1)
        for num in range(1, 9 + 1, 1):

            if self.check_input_validity((row, col, num)):

                grid[row][col] = num.__str__()
                if self.auto_solve(row, col + 1):
                    return True
            grid[row][col] = ''
        return False

    def hint(self):
        pass

    def play(self):
        raise NotImplementedError("specify the mood of play first")

    def getArray(self):
        return self.array

    def print_board(self):
        for line in self.getArray():
            print(line)
'''