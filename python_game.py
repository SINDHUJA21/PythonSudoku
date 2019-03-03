
from __future__ import print_function
import numpy

class PythonGame:

    def __init__(self):

        # create sudoku board
        self.board = numpy.zeros((9,9), dtype = int)
        self.set_vertical_value = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ]
        self.set_horizontal_value = [ each_char.lower() for each_char in self.set_vertical_value ]
    
    def print_horizontal_line(self, number_of_dashes):
        print(number_of_dashes)
        for each in range(0,int(number_of_dashes)):
            print(each)
            print("-", end="")

    def print_vertical_line(self, number_of_dashes):
        for each in range(number_of_dashes):
            print("|")

    def print_horizontal_alphabets(self):
        space_symbol = ' '
        for each in self.set_horizontal_value:
            print(2*space_symbol + each, end=2*space_symbol)

    def print_vertical_alphabets(self):
        space_symbol = ' '
        for each in self.set_vertical_value:
            print(each)

    def form_board(self):

        # feed the  values manually

        self.board[0,0] = 1
        self.board[0,2] = 6
        self.board[0,5] = 2
        self.board[0,6] = 3
        self.board[1,1] = 5
        self.board[1,5] = 6
        self.board[1,7] = 9
        self.board[1,8] = 1
        self.board[2,2] = 9
        self.board[2,3] = 5 
        self.board[2,5] = 1
        self.board[2,6] = 4
        self.board[2,7] = 6
        self.board[2,8] = 2 
        self.board[3,1] = 3
        self.board[3,2] = 7 
        self.board[3,3] = 9
        self.board[3,5] = 5
        self.board[4,0] = 5
        self.board[4,1] = 8
        self.board[4,2] = 1
        self.board[4,4] = 2
        self.board[4,5] = 7
        self.board[4,6] = 9
        self.board[5,3] = 4
        self.board[5,5] = 8
        self.board[5,6] = 1
        self.board[5,7] = 5
        self.board[5,8] = 7
        self.board[6,3] = 2
        self.board[6,4] = 6
        self.board[6,6] = 5
        self.board[6,7] = 4
        self.board[7,2] = 4
        self.board[7,3] = 1
        self.board[7,4] = 5
        self.board[7,6] = 6
        self.board[7,8] = 9
        self.board[8,0] = 9
        self.board[8,3] = 8
        self.board[8,4] = 7
        self.board[8,5] = 4
        self.board[8,6] = 2
        self.board[8,7] = 1
        return self.board


play_game = PythonGame()

print(play_game.form_board())
