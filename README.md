# Sudoku-Game-implementaion
Implementation  of Sudoku game in python. This code generates sudoku board with different difficulty levels or simply reads one from a text file. 
Then, it allows for couple modes of playing; one and two player modes.

To play the game you'll need to install the following libraries:
- random
- copy
- timeit

#
The format of the text file is:

    ,,,3,,2,9,,5
    ,,9,6,4,,7
    ,1,,,,,,,2
    ,5,,,,,,3,6
    2,,3,8,6,5,,7,9
    9,6,1,2,,7,,4,8
    4,,2,,,,,,7
    1,7,,5,2
    ,,,,,4,6

Which represents the board:

          0, 1, 2, 3, 4, 5, 6, 7, 8 
         ---------------------------
    0 :  [0, 0, 0, 3, 0, 2, 9, 0, 5]
    1 :  [0, 0, 9, 6, 4, 0, 7, 0, 0]
    2 :  [0, 1, 0, 0, 0, 0, 0, 0, 2]
    3 :  [0, 5, 0, 0, 0, 0, 0, 3, 6]
    4 :  [2, 0, 3, 8, 6, 5, 0, 7, 9]
    5 :  [9, 6, 1, 2, 0, 7, 0, 4, 8]
    6 :  [4, 0, 2, 0, 0, 0, 0, 0, 7]
    7 :  [1, 7, 0, 5, 2, 0, 0, 0, 0]
    8 :  [0, 0, 0, 0, 0, 4, 6, 0, 0]
