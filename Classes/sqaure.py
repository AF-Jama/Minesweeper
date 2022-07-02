'''Will represent a single sqaure'''


class Sqaure:
    MINE = False # ALL SQAURES ARE ASSUMED TO BE NON MINES
    def __init__(self,x =0,y=0,num=0):
        self.x = x # x coordinate
        self.y = y # y coordinate
        self.num = num # number of adjecent mines


    # def __repr__(self) -> str:
    #     return '*'



class Mine(Sqaure):
    '''A mine is a sqaure with just an added bomb'''
    MINE = True
    def __init__(self, x=0, y=0, num=0):
        super().__init__(x, y, num)




    
# s = Sqaure(1,2)

# print(s)
