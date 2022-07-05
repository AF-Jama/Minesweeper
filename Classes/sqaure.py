'''Will represent a single sqaure'''


class Sqaure:
    # MINE = False # ALL SQAURES ARE ASSUMED TO BE NON MINES
    def __init__(self,x =0,y=0):
        self.x = x # x coordinate
        self.y = y # y coordinate
        self.num = 0 # number of adjecent mines, default is zero
        self.chosen = False # attribute flag to see if sqaure has been chosen already


    def __repr__(self) -> str:
        if self.chosen:    
            '''If chosen show the number of neigbouring mines the sqaure has '''
            return str(self.num)

        return '*' # else just show a normal sqaure



class Mine(Sqaure):
    '''A mine is a sqaure with just an added bomb'''
    # MINE = True
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.num = None


    def __repr__(self):
        if self.chosen:
            return 'x' # if chosen then show mine

        return '*' # else show normal sqaure



    
# s = Sqaure(1,2)

# print(s)
