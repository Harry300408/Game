import pygame, sys, os
from NOQA_Game_Engine.engine import *
from NOQA_Game_Engine.pyvidplayer import *

if __name__ == "__main__":
    game = Engine()
    
    while True:
        game.run()
        pygame.display.flip()