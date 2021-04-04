import os
import pygame
from .config import *

class Drop(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, dir_image):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((40,40))     
        self.image = pygame.image.load(os.path.join(dir_image, 'blood.png'))    
        self.image = pygame.transform.scale(self.image, (40, 40))
        # self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        #Mask
        self.mask = pygame.mask.from_surface(self.image)
        self.vel_x = ELEMENTS_SPEED

    def update(self):
        self.rect.left -= self.vel_x

    def stop(self):
        self.vel_x = 0
    
    def restart(self):
        self.vel_x  = ELEMENTS_SPEED