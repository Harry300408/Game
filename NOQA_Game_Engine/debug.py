import pygame
pygame.init()
from .CONSTANTS import *
font = pygame.font.Font(None,30)

def debug(info,y = 10, x = 10):
    display_suface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, "White").convert_alpha()
    debug_rect = debug_surf.get_rect(topleft = (10, SWthHgh[1] / 2))
    display_suface.blit(debug_surf, debug_rect)