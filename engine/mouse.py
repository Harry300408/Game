import pygame, sys
sys.path.append("././")

class mouse():
    def __init__(self) -> None:
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.get_surface()
        self.location = pygame.mouse.get_pos()
        self.image = pygame.image.load("gfx/gui/mouse/mouse1.png")
        self.imagerect = self.image.get_rect(center=self.location)
        self.wheelofdeath_frame = 0
        
        self.throb = False
        self.throb_anim_time = 200
        self.throb_time = 0

        self.temp = False

    def update_img(self):
        keys = pygame.mouse.get_pressed()

        if keys[0]:
            self.image = pygame.image.load("gfx/gui/mouse/mouse2.png")

        elif self.temp: ## TODO - Update with func
            self.image = pygame.image.load("gfx/gui/mouse/mouse4.png")
        
        elif self.temp: ## TODO - Update with func
            self.image = pygame.image.load("gfx/gui/mouse/mouse3.png")
        
        elif self.temp: ## TODO - Update with func
            if self.wheelofdeath_frame == 8:
                self.wheelofdeath_frame = 0
            
            elif not self.throb: 

                if self.wheelofdeath_frame == 0:
                    self.image = pygame.image.load("gfx/gui/mouse/throbber/frame1.png")
                    self.wheelofdeath_frame += 1
                    self.throb = True
                    self.throb_time = pygame.time.get_ticks() 

                elif self.wheelofdeath_frame == 1:
                    self.image = pygame.image.load("gfx/gui/mouse/throbber/frame2.png")
                    self.wheelofdeath_frame += 1
                    self.throb = True
                    self.throb_time = pygame.time.get_ticks() 
            
                elif self.wheelofdeath_frame == 2:
                    self.image = pygame.image.load("gfx/gui/mouse/throbber/frame3.png")
                    self.wheelofdeath_frame += 1
                    self.throb = True
                    self.throb_time = pygame.time.get_ticks() 
            
                elif self.wheelofdeath_frame == 3:
                    self.image = pygame.image.load("gfx/gui/mouse/throbber/frame4.png")
                    self.wheelofdeath_frame += 1
                    self.throb = True
                    self.throb_time = pygame.time.get_ticks() 
            
                elif self.wheelofdeath_frame == 4:
                    self.image = pygame.image.load("gfx/gui/mouse/throbber/frame5.png")
                    self.wheelofdeath_frame += 1
                    self.throb = True
                    self.throb_time = pygame.time.get_ticks() 
            
                elif self.wheelofdeath_frame == 5:
                    self.image = pygame.image.load("gfx/gui/mouse/throbber/frame6.png")
                    self.wheelofdeath_frame += 1
                    self.throb = True
                    self.throb_time = pygame.time.get_ticks() 
            
                elif self.wheelofdeath_frame == 6:
                    self.image = pygame.image.load("gfx/gui/mouse/throbber/frame7.png")
                    self.wheelofdeath_frame += 1
                    self.throb = True
                    self.throb_time = pygame.time.get_ticks() 
            
                elif self.wheelofdeath_frame == 7:
                    self.image = pygame.image.load("gfx/gui/mouse/throbber/frame8.png")
                    self.wheelofdeath_frame += 1
                    self.throb = True
                    self.throb_time = pygame.time.get_ticks() 

        else:
            self.image = pygame.image.load("gfx/gui/mouse/mouse1.png")
    
    def throbcooldown(self):
        current_time = pygame.time.get_ticks()
        if self.throb:
            if current_time - self.throb_time >= self.throb_anim_time:
                self.throb = False

    def update(self):
        self.location = pygame.mouse.get_pos()
        self.throbcooldown()
        self.update_img()
        self.imagerect = self.image.get_rect(center=self.location)
        self.screen.blit(self.image, self.imagerect)