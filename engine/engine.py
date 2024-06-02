import pygame, sys
from .CONSTANTS import *
from .debug import *
from .mouse import *

class Engine():
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_mode((SWIDTH, SHEIGHT), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.clock = pygame.Clock()
        self.fps = self.clock.get_fps()
        self.screen = pygame.display.get_surface()
        self.mouse = mouse()
        self.icon = pygame.image.load("././gfx/icon.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("The Apocalyptic Nomad")
    
    def update(self):
        self.screen.fill("black")
        self.clock.tick()
        self.fps = self.clock.get_fps()
        
        self.mouse.update()

        debug(str(round(self.fps)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()