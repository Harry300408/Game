import pygame, sys, os
from .player import *

class Level():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()    

        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group() 

        self.load_level()
        
    def load_level(self):
        self.player = Player([self.visible_sprites])
    
    def update(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()