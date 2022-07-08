'''Board class - Will represent the board that will be played on on'''
from abc import ABC,abstractmethod
from random import randint
import numpy as np
from Classes.sqaure import Sqaure,Mine

# Base board which represents a 
class BaseBoard(ABC):
    def __init__(self,width = 9, height = 9) -> None:
        super().__init__()
        self.width = width
        self.height = height
        # self.sqaure = Sqaure() # compisition as board has sqaures
        # self.mine = Mine() # compisition as board has mine
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
                self.board[index] = Sqaure()

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
                    self.board[row][col].num +=1
                    # num_of_bombs+=1 # increments number of bombs surronding sqaure
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

            self.board[position] = Mine() # adds mine into this 
            number_of_mines+=1
        return self.board # returns board with sqaures and mines


    def choose_cell(self,row,col):
        '''There are three possible actions that can occur here

        1) Mine hit causing the game to end
        2) Sqaure hit with atleast 1 neighbouring mine. meaning sqaure is shown to user
        3) Sqaure with no neighbouring mines, is recursively searched up till sqaures with neighbouring mines
        '''

        if isinstance(self.board[row][col],Mine):
            return False

        if self.board[row][col].num>0 and self.board[row][col].chosen!=True:
            self.board[row][col].chosen = True # Now Cannot chosen on further picks
            return True

        if self.board[row][col].num== 0 and self.board[row][col].chosen!=True:
            '''Triggered if sqaure has no neighbouring mines then iteravily searched uptil sqaures with neighbouring mines'''
            self.board[row][col].chosen = True
            for r in range(max(0,row-1),min(self.height-1,(row+1)+1)): # increments through all sqaures in row -> 0- 2 col ->0->2
                for c in range(max(0,col-1),min(self.width-1,(col+1)+1)):
                    if self.board[r][c].chosen == True and isinstance(self.board[r][c],Sqaure):
                        '''Triggered when sqaure is already chosen and doesnt need to re dug'''
                        continue

                    self.choose_cell(r,c) # recursive use of function

            return True


    def check_all_sqaures(self):
        '''Checks if all sqaures have been attribute value true'''
        for row in range(self.height):
            for col in range(self.width):
                if isinstance(self.board[row][col],Sqaure) and self.board[row][col].chosen == True:
                    continue

                elif isinstance(self.board[row][col],Mine):
                    pass

                else:
                    break

            return False

        return True


    def show_current_board(self):
        return self.board


    def check_bounds(self,row,col)->bool:
        '''Check bounds of cell choosen'''
        if col<0 or row<0 or col>self.width-1 or row>self.height-1 or self.board[row][col].chosen == True:
            return True

        return False 
    
    @property
    def show_solved_board(self):
        '''Show full solved beard'''
        for r in range(self.width):
            for c in range(self.height):
                if isinstance(self.board[r][c],Mine):
                    self.board[r][c].chosen = True

                if (isinstance(self.board[r][c],Sqaure)):
                    self.board[r][c].chosen = True

        return self.board # returns solved board


    
    def run(self):
        while not self.check_all_sqaures():
            print(self.show_current_board())
            coordinate = input("Enter coordinate ie:(x,y):")
            # print(coordinate)
            x,y = coordinate.split(',')
            x = int(x)
            y = int(y)
            if(self.check_bounds(x,y)):
                print("Invalid Coordinate or sqaure has already been chosen")
                continue

            success = self.choose_cell(x,y)
            if success:
                continue

            else:
                print("HIT A MINE")
                break

        
        if success:
            print("YOU WON!!")

        else:
            print("Solved Board:")
            print(self.show_solved_board)

        



    def __repr__(self) -> str:
        a = np.array(self.board).reshape(self.width,self.height)
        return str(a)


if __name__ == "__main__":
    b = Board()
    b.run()