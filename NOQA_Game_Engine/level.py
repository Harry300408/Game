import pygame, sys, os
from random import *
from .CONSTANTS import *; from .player import *; from .tile import *; from .support import *

class Level():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        
        # CAMERA    
        self.visible_sprites = pygame.sprite.Group()
        self.camera_top = pygame.sprite.Group()
        self.camera_middle = pygame.sprite.Group() ## FOR PLAYERS AND NPCS
        self.camera_bottom = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group() ## PLAYER ONLY
        
        self.obstacles_sprites = pygame.sprite.Group() 
        
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        
        self.scale = 1.2
        
        ## OTHER
        self.count = 0
        self.list = []

        self.load_level()
        
    def load_level(self):
        for i in range(0, 25):
            rand_x = randint(0, SWthHgh[0])
            rand_y = randint(0, SWthHgh[1])
            tile([self.camera_bottom, self.visible_sprites, self.obstacles_sprites], (rand_x, rand_y), "tree_bottom")
            tile([self.camera_top ,self.visible_sprites, self.obstacles_sprites], (rand_x, rand_y), "tree_top")
        
        self.player = Player([self.camera_middle, self.visible_sprites, self.player_group], (self.half_w, self.half_h))
        
        for i in self.visible_sprites:
            i.image = pygame.transform.scale(i.image, (i.image.get_width() * self.scale, i.image.get_height() * self.scale)).convert_alpha()
            i.rect = i.image.get_rect(center = i.pos)
    
        
    def update(self):  
        self.visible_sprites.update()    
        
        self.offsetx = self.player.rect.centerx - self.half_w
        self.offsety = self.player.rect.centery - self.half_h
        
        for i in self.visible_sprites:
            i.rect.x -= self.offsetx
            i.rect.y -= self.offsety 
                     
        self.camera_bottom.draw(self.display_surface)
        self.camera_middle.draw(self.display_surface)
        self.camera_top.draw(self.display_surface)
        self.player.player_ui.update(self.player.maxhp, self.player.maxmana, self.player.maxrads, self.player.maxexp)