'''Player class - Each game will be played by one player'''
from Classes.board import Board
from Classes.sqaure import Sqaure,Mine

class Player:
    def __init__(self,name):
        self.board = Board() # player has a board
        self.name = name

    def choose_cell(self,col,row):
        '''Allow player to choose cell to click'''
        if(self.check_bounds(col,row)):
            print("Invalid sqaure")
            return


        if (isinstance(self.board.board[(col*row)-1],Mine)):
            '''If mine is choose game is over'''
            print("Game Over, You hit a mine")
            return

        if (isinstance(self.board.board[(col*row)-1],Sqaure)):
            '''We want to create logic here that checks the neigbours of each sqaure'''
            pass


        def search_for_neighbours(self):
            pass

    def check_bounds(self,col,row)->bool:
        '''Check bounds of cell choosen'''
        if col<0 or row<0 or col>self.board.width-1 or row>self.board.height-1:
            return True

        return False 



p = Player()
p.choose_cell(5,5)