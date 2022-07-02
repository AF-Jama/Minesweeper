'''Board class - Will represent the board that will be played on on'''
from abc import ABC,abstractmethod
from random import randint
from sqaure import Sqaure,Mine

# Base board which represents a 
class BaseBoard(ABC):
    def __init__(self,width = 9, length = 9) -> None:
        super().__init__()
        self.width = width
        self.length = length
        self.sqaure = Sqaure() # compisition as board has sqaures
        self.mine = Mine() # compisition as board has mine
        self.board = []

    @abstractmethod
    def createStructure(self):
        '''creates structure of board'''
    
    @abstractmethod 
    def add_random_mines(self):
        pass



class BegineerBoard(BaseBoard):
    '''Begineer board with a 9x9 structure and 10 mines in total'''
    DIFFUCULTY = "BEGINEER"
    MINES = 10
    def __init__(self, width=9, length=9) -> None:
        super().__init__(width, length)

    def createStructure(self):
        '''creates structure of board, ie: placing mines in random locations'''
        self.board = [0 for l in range(self.length) for w in range(self.width)] # creating board with length and width
        self.add_random_mines() # adds mines to board in random areas between 0 and 81
        self.add_sqaures() # adds sqaures in areas where there are no mines
        return self.board 

    def add_random_mines(self):
        '''Adding mines in random positions'''
        for i in range(BegineerBoard.MINES):
            position = abs(randint(1000,2000) %(self.width*self.length)-1-i) # gets random position between index 0 and (self.width*self.length)-1
            self.board[position] = self.mine # adds mine into this 

        return self.board # returns board with sqaures and mines

    def add_sqaures(self):
        '''Adding sqaures to everywhere that is not a mine'''
        for index,element in enumerate(self.board):
            if(not isinstance(element,Mine)):
                '''When sqaure is not an instance of the Mine class we add a generic sqaure in that position'''
                self.board[index] = self.sqaure




b = BegineerBoard()
print("=======")
print(b.createStructure())

