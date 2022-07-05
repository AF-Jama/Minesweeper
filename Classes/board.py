'''Board class - Will represent the board that will be played on on'''
from abc import ABC,abstractmethod
from random import randint
import numpy as np
from sqaure import Sqaure,Mine

# Base board which represents a 
class BaseBoard(ABC):
    def __init__(self,width = 9, height = 9) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.sqaure = Sqaure() # compisition as board has sqaures
        self.mine = Mine() # compisition as board has mine
        self.board = []

    def createStructure(self):
        '''creates structure of board, ie: placing mines in random locations'''
        self.board = [0 for l in range(self.height) for w in range(self.width)] # creating board with length and width
        self.add_random_mines() # adds mines to board in random areas between 0 and 81
        self.add_sqaures() # adds sqaures in areas where there are no mines
        self.board = np.array(self.board).reshape(self.width,self.height) # reshape flat array into numpy array
        self.assign_numbers_to_sqaures()
        return self.board 
    
    @abstractmethod
    def add_random_mines(self):
        '''Adding mines in random positions depending on the diffuculty of the board'''

    def add_sqaures(self):
        '''Adding sqaures to everywhere that is not a mine'''
        for index,element in enumerate(self.board):
            if(not isinstance(element,Mine)):
                '''When sqaure is not an instance of the Mine class we add a generic sqaure in that position'''
                self.board[index] = self.sqaure

    def assign_numbers_to_sqaures(self):
        '''Iterating through'''
        for row in range(self.height):
            for col in range(self.width):
                if (isinstance(self.board[row][col],Mine)):
                    '''If its a mine then we do nothing to it. We only want to calculate the surronding mines for an empty sqaure'''
                    continue # carry on loop without doing anything here

                self.calc_numbers_on_sqaures(row,col) # all sqaures are processed here 

    def calc_numbers_on_sqaures(self,row,col):
        num_of_bombs = 0 # counter for bombs
        for r in range(max(0,row-1),min(self.height-1,(row+1)+1)): # increments through all sqaures in row
            for c in range(max(0,col-1),min(self.width-1,(col+1)+1)):
                if r==row and c == col:
                    '''Triggered if row and column is same as the one being referenced'''
                    # print("Same coordinate")
                    continue
                if(isinstance(self.board[r][c],Mine)):
                    num_of_bombs+=1 # increments number of bombs surronding sqaure
                    

        
        return self.board


class Board(BaseBoard):
    '''Begineer board with a 9x9 structure and 10 mines in total'''
    DIFFUCULTY = "BEGINEER"
    MINES = 10
    def __init__(self, width=9, height=9) -> None:
        super().__init__(width, height)
        self.createStructure() # creates structure of board on initialisation
        
    def add_random_mines(self):
        '''Adding mines in random positions'''
        number_of_mines = 0
        while number_of_mines< Board.MINES:
            position = abs(randint(1000,2000) %(self.width*self.height)-1-number_of_mines) # gets random position between index 0 and (self.width*self.length)-1
            if (isinstance(self.board[position],Mine)):
                continue

            self.board[position] = self.mine # adds mine into this 
            number_of_mines+=1
        return self.board # returns board with sqaures and mines


    def show_board(self):
        a = np.array(self.board).reshape(self.width,self.height)
        print(a)


    # def assign_numbers_to_sqaures(self):
    #     '''Iterating through'''
    #     for row in self.board:
    #         for col in row:
    #             if (isinstance(self.board[row][col],Mine)):
    #                 '''If its a mine then we do nothing to it. We only want to calculate the surronding mines for an empty sqaure'''
    #                 continue # carry on loop without doing anything here

    #             self.calc_numbers_on_sqaures(row,col) # all sqaures are processed here 

    # def calc_numbers_on_sqaures(self,row,col):
    #     num_of_bombs = 0 # counter for bombs
    #     for r in range(row-1, (row+1)+1): # increments through all sqaures in row
    #         for c in range(col-1,(col+1)+1):
    #             if(isinstance(self.board[r][c],Mine)):
    #                 num_of_bombs+=1 # increments number of surronding bombs

    #     self.board[row][col].num = num_of_bombs # assigns number of surronding bombs










b = Board()
print("=======")
# b.show_board()

# for row in b.board:
#     for col in row:
#         if(isinstance(col,Mine)):
#             print("Is a sqaure")

#         else:
#             print("Is a mine")


print(b.board)

