
from __future__ import print_function
import numpy
import time

class PythonGame:

    def __init__(self):

        # create sudoku board
        self.board = numpy.zeros((9,9), dtype = int)
        self.set_vertical_value = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ]
        self.set_horizontal_value = [ each_char.lower() for each_char in self.set_vertical_value ]
        self.space_symbol = ' '
    
    def print_horizontal_line(self, number_of_dashes):
        for each in range(0,int(number_of_dashes)):
            print("-", end="")

    def print_horizontal_alphabets(self):
        print("|", end="")
        for each in self.set_horizontal_value:
            print(2*self.space_symbol + each, end=2*self.space_symbol)
            print("|", end="")

    def print_new_line(self):
        print("\n")

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

    def print_board(self):
        # self.print_horizontal_line(55)
        self.print_new_line()
        self.print_horizontal_alphabets()
        self.print_new_line()
        self.print_horizontal_line(55)
        self.print_new_line()
        count = 1
        iterate = 0
        print("|", end="")
        for each_val in numpy.nditer(self.form_board()):
            if each_val == 0:
                each_val = " "
            print(2*self.space_symbol + "{}".format(each_val), end=2*self.space_symbol)
            print("|", end="")
            count+=1
            if count > 9:
                print(2*self.space_symbol + self.set_vertical_value[iterate])
                iterate+=1
                count = 1
                self.print_horizontal_line(55)      
                print("\n")    
                print("|", end="")



play_game = PythonGame()

print("Welcome !!! Let's play sudoko:")
print("Board will be presented here:")
time.sleep(2)
play_game.print_board()
print("Lets start the game. Fill the empty spaces with relevant values. To update the board specify the horizontal and vertical character: (eg : a,B=2)\n")
# get_values = input()