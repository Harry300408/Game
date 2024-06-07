import pygame, sys, os
from .level import *; from .mouse import *; from .debug import *; from .CONSTANTS import *; from .pyvidplayer import *; from .functions.getfont import *; from .mainmenu.mainmenu import *

class Engine(): ## NO-QA SUB-ENGINE
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SWthHgh, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.mouse = mouse()
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.display = pygame.display.get_surface()
        pygame.display.set_caption("The Apocalyptic Nomad")
        pygame.display.set_icon(pygame.image.load("././gfx/icon.png"))
        
        self.HINT_TEXT = get_px1_font(20).render("Click To Go To Main Menu", True, "white")
        self.HINT_TEXT_RECT = self.HINT_TEXT.get_rect(bottomright=( SWthHgh[0], SWthHgh[1]))
        
        self.main_menu = MainMenu()
        
        self.oldfps = 0
        
        self.video = Video("././" + SPLASH_LOC)
        self.video.set_size(SWthHgh)
        self.is_playing = True
        self.intro()
    
        
    
    def intro(self):
        while self.is_playing:
            self.screen.fill("black")
            self.video.draw(self.display, (0,0))
            self.screen.blit(self.HINT_TEXT, self.HINT_TEXT_RECT)
            self.mouse.update()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        self.video.close()
                        self.is_playing = False

    def run(self):
        if self.main_menu.in_menu:
            self.main_menu.update()
            
        else:
            self.screen.fill("black")
            self.clock.tick(SFPS)
            self.fps = self.clock.get_fps()
            self.level.update()
        
            debug(str(round(self.fps)))
            
            if self.fps > self.oldfps:
                self.oldfps = self.fps
                print("Highest FPS So Far: " + str(self.oldfps))
        
            self.mouse.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            