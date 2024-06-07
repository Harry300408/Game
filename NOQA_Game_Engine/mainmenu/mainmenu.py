import pygame, sys
from ..functions.getfont import *
from ..CONSTANTS import *
from ..mouse import *
from ..debug import *
from ..support import *
from .button import *


class MainMenu():
    def __init__(self):
        self.in_menu = True
        self.MENU_TXT = get_px2_font(100).render("THE APOCALYPTIC NOMAD", True, "white")
        self.MENU_TXT_RECT = self.MENU_TXT.get_rect(center = (SWthHgh[0] / 2, 100))
        
        pygame.mixer.music.load("./././" + MM_Music)
        self.firecrackle = pygame.mixer.Sound("./././" + MM_FireCracks)
        pygame.mixer.music.set_volume(0.2)
        
        self.mouse = mouse()
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        
        self.mm_sounds_playing = False
        self.oldfps = 0
        
        self.vignette = pygame.image.load("./././gfx/vignette/Vignette.png").convert_alpha()
        self.vignette = pygame.transform.scale(self.vignette, SWthHgh)
        self.vignette_rect = self.vignette.get_rect(topleft=(0,0))
        
        self.campfire_anims = []
        self.campfire_frame = 0.1
        self.load_campfire_anims()
        self.campfire_img = self.campfire_anims[int(self.campfire_frame)]
        self.campfire_img = pygame.transform.scale(self.campfire_img, (self.campfire_img.get_width() * 4, self.campfire_img.get_height() * 4)) 
        self.campfire_rect = self.campfire_img.get_rect(center = (SWthHgh[0] / 3, SWthHgh[1] / 2.8))
        
        self.play_button = Button(None, (SWthHgh[0] / 1.5, SWthHgh[1] / 4), "PLAY", get_px1_font(50), "white", "orange", None)
        self.settings_button = Button(None, (SWthHgh[0] / 1.5, SWthHgh[1] / 2.65), "SETTINGS", get_px1_font(50), "white", "orange", None)
        self.quit_button = Button(None, (SWthHgh[0] / 1.5, SWthHgh[1] / 2), "QUIT", get_px1_font(50), "white", "orange", None)

    
    def load_campfire_anims(self):
        self.campfire_anims = import_folder("./././gfx/campfire")
    def load_mm_sounds(self):
        if not self.mm_sounds_playing:
            self.mm_sounds_playing = True
            pygame.mixer.music.play(-1)
            pygame.mixer.Channel(0).play(self.firecrackle, -1)
    
    def update(self):
        self.screen.fill(MM_PURPLE)
        self.load_mm_sounds()
        dt = self.clock.tick(SFPS)
        
        self.campfire_frame += 0.01 * dt
        if self.campfire_frame > 7:
            self.campfire_frame = 0.1
            
        self.campfire_img = self.campfire_anims[int(self.campfire_frame)]
        self.campfire_img = pygame.transform.scale(self.campfire_img, (self.campfire_img.get_width() * 4, self.campfire_img.get_height() * 4)) 
        
        self.fps = self.clock.get_fps()
        
        self.screen.blits([
                           (self.vignette, self.vignette_rect),
                           (self.campfire_img, self.campfire_rect),
                           (self.MENU_TXT, self.MENU_TXT_RECT)
                           ])
        
        for i in [self.play_button, self.settings_button, self.quit_button]:
            i.changeColor(self.mouse.location)
            i.update(self.screen)
        
        debug(str(round(self.fps)))
        
        
        self.fps = self.clock.get_fps()
            
        if self.fps > self.oldfps:
            self.oldfps = self.fps
            print("Highest FPS So Far: " + str(self.oldfps))
            
        self.mouse.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if pygame.mouse.get_pressed()[0]:
                    
                    if self.play_button.checkForInput(self.mouse.location):
                        self.in_menu = False
                        self.mm_sounds_playing = False
                        pygame.mixer.music.pause()
                        pygame.mixer.Channel(0).pause()
                    
                    if self.quit_button.checkForInput(self.mouse.location):
                        pygame.quit()
                        sys.exit()      
                        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()