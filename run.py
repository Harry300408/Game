from engine.engine import *

if __name__ == "__main__":
    game = Engine()
    
    while True:
        game.update()
        pygame.display.flip()