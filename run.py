#import os
#import sys
#path = os.path.dirname(os.path.realpath(__file__))
#sys.path=[path+"\src\maps"]+[path+"/src/maps"]+[path+"/src"]+[path+"\src"]+sys.path

from main.game import game

if __name__ == "__main__":
    
    main_game = game()
    #game.Run()

