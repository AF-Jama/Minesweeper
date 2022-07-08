import re
from Classes.board import Board

class Game():
    def play(self):
        play_now = True
        while play_now:
            '''Infinte while loop'''
            b = Board()
            b.run()
            user_continue = input("Do you want to continue (y or any other key to exit)")
            user_continue = user_continue.lower()
            if user_continue == 'y':
                play_now = True

            else:
                break



g = Game()
g.play()