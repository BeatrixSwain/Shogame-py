import pygame
from .config import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, width, height, color, left, bottom):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
        self.start = left
        self.vel_x = WALL_SPEED

    def update(self):
        self.rect.left -=  self.vel_x 
        # if self.rect.left<0: #Para que se reinicie
        #     self.rect.left = self.start

    def stop(self):
        self.vel_x  = 0

    def restart(self):
        self.vel_x  = WALL_SPEED