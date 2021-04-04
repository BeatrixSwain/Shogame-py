import os
import pygame
from .config import *

class Player(pygame.sprite.Sprite):

    def __init__(self, left, bottom, floor, dir_image):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((WIDTH_PLAYER,HEIGHT_PLAYER))
        # self.image.fill(ORANGE)
        
        self.images = (
             pygame.image.load(os.path.join(dir_image, 'doll.png')),
             pygame.image.load(os.path.join(dir_image, 'crow.png'))
        )    
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        #MASK
        self.mask = pygame.mask.from_surface(self.image)

        # self.rect.x = 100
        # self.rect.y = 100
        self.rect.left = left
        self.rect.bottom = bottom
        self.pos_y = self.rect.bottom
        self.vel_y = 0
        self.falling = True
        self.floor = floor
        # self.can_jump = False
        self.can_jump = True
        self.playing = True

    def update_pos(self):
        if self.vel_y < 0: #Salto
            self.vel_y += PLAYER_GRAV #Papel de la gravedad
            if((self.pos_y + self.vel_y + 0.5* PLAYER_GRAV)<HEIGHT_PLAYER):#Evitar que se vaya de pantalla.
                self.pos_y = HEIGHT_PLAYER
                self.vel_y = 0
            else:
                self.pos_y += self.vel_y + 0.5* PLAYER_GRAV    
        elif self.pos_y >= self.floor: #Ha llegado al suelo
            self.vel_y = 0
            self.can_jump = True            
        else:
            self.vel_y += PLAYER_GRAV #Papel de la gravedad
            self.pos_y += self.vel_y + 0.5*  PLAYER_GRAV  
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (50, 50))  
    
    def update(self):
        if self.playing:
            self.update_pos()
            self.rect.bottom = self.pos_y

    def validate_platform(self, platform):
        res = pygame.sprite.collide_rect(self, platform) #Colision, para detener la caida
        if res:
            self.vel_y=0
            self.pos_y = platform.rect.top
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (50, 50))
            
        
    def jump(self):
        if self.can_jump:
            self.vel_y =  JUMP
            self.image = self.images[1]
            self.image = pygame.transform.scale(self.image, (50, 50))
            # self.can_jump = False

    def collide_with(self, sprites):
        #Si existe colisión retorna una lista de con los que hay colision:
        obj = pygame.sprite.spritecollide(self, sprites, False)#El que queremos que compare si ha chocado, lista de sprites, 
        if obj:
            return obj[0] #Retornamos el primero con el que ha chocado
        
    def stop(self):
        # self.playing = False
        pass

    def collide_bottom(self, wall):
        return self.rect.colliderect(wall.rect_top)

    def skid(self, wall):
        # print("Esquiando")
        self.pos_y = wall.rect.top
        self.vel_y = 0
        self.can_jump = True
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (50, 50))