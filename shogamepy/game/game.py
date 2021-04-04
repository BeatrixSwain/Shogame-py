import sys
import pygame
# path = 'C:\Proyectos 2021\Shogamepy\Shogame-py\shogamepy\\'
# sys.path.append(path)
from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall
import random

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.running = True #Para saber si la aplicación se está ejecutando o no.
        self.calm_down = CALM_DOWN
        self.move = MOVE_SPEED
        self.playing = True
        self.stop_horizontal = LOSE_IF_HORIZONTAL_COL

    def start(self):
        self.new()

    def generate_elements(self):
        #Plataforma
        self.platform = Platform()
        self.sprites = pygame.sprite.Group()#Agrupar diferentes sprites que se usarán en el juego: plataforma, personaje, monedas...
        self.sprites.add(self.platform)
        #Jugador
        self.player = Player(100, self.platform.rect.top-200, self.platform.rect.top) #Lo colocamos en x 100 y en la parte más alta de la plataforma. - Se hace que caiga de una altura de 200
        self.sprites.add(self.player)
        #Obstáculo
        # self.wall = Wall(40,100,RED, WIDTH, self.platform.rect.top)
        # self.sprites.add(self.wall)
        self.walls = pygame.sprite.Group()
        self.generateWalls()
    
    def generateWalls(self):
        last_position = WIDTH+100
        if not len(self.walls)>0:
            for w in range(0,MAX_WALLS):
                left = random.randrange(last_position+200, last_position+400)
                wall = Wall(40,  random.randrange(100, 300), RED, left,  self.platform.rect.top)
                last_position = wall.rect.right
                self.sprites.add(wall)
                self.walls.add(wall)

    
    def new(self):
        self.generate_elements()
        self.run()

    def run(self):
        while(self.running):
            pygame.time.delay(self.calm_down)
            self.events()
            self.draw()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Cuando se hace click en el botón cerrar
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.player.jump()

    def draw(self):
        self.surface.fill(WHITE)
        self.sprites.draw(self.surface)

    def update(self):
        if self.playing:
            pygame.display.flip()#ACTUALIZA LA PANTALLA, SE HARÁ SOBRE TODA LA SUPERFICIE.
            wall = self.player.collide_with(self.walls)
            if wall:
                self.stop()
            else:
                if not self.stop_horizontal:
                    self.reestartmove()
            self.sprites.update()
            self.player.validate_platform(self.platform)
           

    
    def stop(self):
        if self.stop_horizontal:
            self.player.stop()
            self.stopelements(self.walls)
            self.playing = False
        else:
            self.stopelements(self.walls)


    def stopelements(self, elements):
        for element in elements:
            element.stop()

    
    def reestartmove(self):
        self.returnMoveWalls(self.walls)
    
    def returnMoveWalls(self, elements):
        for element in elements:
            element.restart()
