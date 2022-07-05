'''Will represent a single sqaure'''


class Sqaure:
    MINE = False # ALL SQAURES ARE ASSUMED TO BE NON MINES
    def __init__(self,x =0,y=0):
        self.x = x # x coordinate
        self.y = y # y coordinate
        self.num = 0 # number of adjecent mines, default is zero
        self.chosen = False # attribute flag to see if sqaure has been chosen already


    def __repr__(self) -> str:
        # # return str(self.num)
        return str(self.num)
        # return '*'



class Mine(Sqaure):
    '''A mine is a sqaure with just an added bomb'''
    MINE = True
    def __init__(self, x=0, y=0):
        super().__init__(x, y)


    def __repr__(self):
        return 'x'



    
# s = Sqaure(1,2)

# print(s)
