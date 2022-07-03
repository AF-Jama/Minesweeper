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



class Board(BaseBoard):
    '''Begineer board with a 9x9 structure and 10 mines in total'''
    DIFFUCULTY = "BEGINEER"
    MINES = 10
    def __init__(self, width=9, height=9) -> None:
        super().__init__(width, height)
        self.createStructure() # creates structure of board on initialisation
        
    def add_random_mines(self):
        '''Adding mines in random positions'''
        for i in range(Board.MINES):
            position = abs(randint(1000,2000) %(self.width*self.height)-1-i) # gets random position between index 0 and (self.width*self.length)-1
            self.board[position] = self.mine # adds mine into this 

        return self.board # returns board with sqaures and mines


    def show_board(self):
        a = np.array(self.board).reshape(self.width,self.height)
        print(a)





b = Board()
print("=======")
b.show_board()

