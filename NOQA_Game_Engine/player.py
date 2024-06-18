import pygame, sys, os
from .CONSTANTS import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos) -> None:
        super().__init__(groups)
        self.pos = pos
        
        self.screen = pygame.display.get_surface()
        
        self.image = pygame.image.load("././gfx/player/test.png").convert_alpha()
        self.rect = self.image.get_rect(center = self.pos)
        self.hitbox = self.rect.inflate(0, -26)

        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(SFPS)
        
        self.speed = 0.5
        
        self.maxhp = 100
        self.maxmana = 75
        self.maxrads = 1000
        self.maxexp = 100
        
        self.player_ui = self._HUD(self.maxhp, self.maxmana, self.maxrads, self.maxexp)
        
    def input(self):
        keys = pygame.key.get_pressed()
        jkeys = pygame.key.get_just_pressed()
        self.dt = self.clock.tick(SFPS)
        self.speed = 0.5
        self.speed *= self.dt
            
        if keys[pygame.K_w]:    
            self.rect.y -= int(self.speed)
        elif keys[pygame.K_s]:    
            self.rect.y += int(self.speed)
        else:
            pass
            
        if keys[pygame.K_a]:    
            self.rect.x -= int(self.speed)
        elif keys[pygame.K_d]:    
            self.rect.x += int(self.speed)
        else:
            pass
        
        if jkeys[pygame.K_l]: 
            self.player_ui.rads = self.player_ui.rads + 10
    
    class _HUD():
        def __init__(self, maxhp, maxmana, maxrads, maxexp):
            self.screen = pygame.display.get_surface()
            
            self.hp = 100
            self.oldhp = self.hp
            self.mana = 75
            self.oldmana = self.mana
            self.rads = 0
            self.oldrads = self.rads
            
            self.hp_ratio = self.hp / maxhp
            self.mana_ratio = self.mana / maxmana
            self.rads_ratio = self.rads / maxrads
            
            self._init_gfx()
            self.calc_bars_nums(maxhp, maxmana, maxrads, maxexp)
        
        def _init_gfx(self):
            ## PLAYER STATUS BARS ##
            self.main_bars_fg = pygame.image.load("././gfx/gui/hud/Health_and_mana_bar/health_and_mana_outline.png").convert_alpha()
            self.main_bars_fg_rect = self.main_bars_fg.get_rect(topleft = (0,0))
            self.hp_bg = pygame.image.load("././gfx/gui/hud/Health_and_mana_bar/hp_bg.png").convert_alpha()
            self.hp_bg_rect = self.hp_bg.get_rect(topleft = (85,11))
            self.hp_bar = pygame.image.load("././gfx/gui/hud/Health_and_mana_bar/hp_bar.png").convert_alpha()
            self.hp_bar_rect = self.hp_bar.get_rect(topleft = (85,11))
            self.mana_bg = pygame.image.load("././gfx/gui/hud/Health_and_mana_bar/mana_bg.png").convert_alpha()
            self.mana_bg_rect = self.mana_bg.get_rect(topleft = (85,44))
            self.mana_bar = pygame.image.load("././gfx/gui/hud/Health_and_mana_bar/mana_bar.png").convert_alpha()
            self.mana_bar_rect = self.mana_bar.get_rect(topleft = (85,44))
            self.player_circle = pygame.image.load("././gfx/gui/hud/Health_and_mana_bar/player_circle.png").convert_alpha()
            self.player_circle_rect = self.player_circle.get_rect(topleft = (0,0))
            self.player_lvl_circle = pygame.image.load("././gfx/gui/hud/Health_and_mana_bar/level_circle.png").convert_alpha()
            self.player_lvl_circle_rect = self.player_lvl_circle.get_rect(topleft = (0,0))
            
            ## GEIGER METER ##
            self.geiger_bar = pygame.image.load("././gfx/gui/hud/Geiger_meter/Geiger_meter_bar.png").convert_alpha()
            self.geiger_bar_rect = self.geiger_bar.get_rect(topleft = (75,68))
            self.safe_rad = pygame.image.load("././gfx/gui/hud/Geiger_meter/safe_rad_bar.png").convert_alpha()
            self.safe_rad_rect = self.safe_rad.get_rect(topleft = (113,74))
            self.rads_bar = pygame.image.load("././gfx/gui/hud/Geiger_meter/rad_amount_bar.png").convert_alpha()
            self.rads_bar_rect = self.rads_bar.get_rect(topleft = (113,74))
            self.rads_bar = pygame.transform.scale(self.rads_bar, (182 * self.rads_ratio, self.rads_bar.get_height()))
        
        def calc_bars_nums(self, maxhp, maxmana, maxrads, maxexp):
            if self.oldhp != self.hp:
                
                if self.hp < 0:
                    self.hp = 0
                elif self.hp > maxhp:
                    self.hp = maxhp
                
                self.oldhp = self.hp
                self.hp_ratio = self.hp / maxhp
                self.hp_bar = pygame.transform.scale(self.hp_bar, (433 * self.hp_ratio, self.hp_bar.get_height()))
            
            if self.oldmana != self.mana:
                
                if self.mana < 0:
                    self.mana = 0
                elif self.mana > maxmana:
                    self.mana = maxmana
                    
                self.oldmana = self.mana
                self.mana_ratio = self.mana / maxmana
                self.mana_bar = pygame.transform.scale(self.mana_bar, (261 * self.mana_ratio, self.mana_bar.get_height()))
            
            if self.oldrads != self.rads:
                
                if self.rads < 0:
                    self.rads = 0
                elif self.rads > maxrads:
                    self.rads = maxrads
                    
                self.oldrads = self.rads
                self.rads_ratio = self.rads / maxrads
                self.rads_bar = pygame.transform.scale(self.rads_bar, (182 * self.rads_ratio, self.rads_bar.get_height()))
        
        def draw_to_screen(self):
            self.screen.blits([## HP & MANA BARS BG ##
                               (self.hp_bg, self.hp_bg_rect),
                               (self.hp_bar, self.hp_bar_rect),
                               (self.mana_bg, self.mana_bg_rect),
                               (self.mana_bar, self.mana_bar_rect),
                               
                               ## HP & MANA BARS ##
                               
                               ## MAIN GFX FOR BARS ##
                               (self.main_bars_fg, self.main_bars_fg_rect),
                               
                               # PLAYER CIRCLE #
                               (self.player_circle, self.player_circle_rect),
                               
                               # GEIGER BAR ##
                               (self.safe_rad, self.safe_rad_rect),
                               (self.rads_bar, self.rads_bar_rect),
                               (self.geiger_bar, self.geiger_bar_rect),
                               
                               # PLAYER LEVEL CIRCLE #
                               (self.player_lvl_circle, self.player_lvl_circle_rect)
                               
                               ])
        
        def update(self, maxhp, maxmana, maxrads, maxexp):
            self.calc_bars_nums(maxhp, maxmana, maxrads, maxexp)
            self.draw_to_screen()
        
    def update(self):
        self.input()