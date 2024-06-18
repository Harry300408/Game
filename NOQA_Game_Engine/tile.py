import pygame, sys, os
from .CONSTANTS import *

class tile(pygame.sprite.Sprite):
    def __init__(self, groups, pos, img) -> None:
        super().__init__(groups)
        self.pos = pos        
        self.screen = pygame.display.get_surface()
        self.img = img
        
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(SFPS)
        self.set_img()
        
    def set_img(self):
        self.image = pygame.image.load("././gfx/tiles/" + self.img + ".png").convert_alpha()
        self.rect = self.image.get_rect(topleft = self.pos)
        self.hitbox = self.rect.inflate(0, -26)
    
    def update(self):
        pass   