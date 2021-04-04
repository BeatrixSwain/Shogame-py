import os
import sys
import pygame
from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall
from .drop import Drop
import random

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.running = True #Para saber si la aplicación se está ejecutando o no.
        self.calm_down = CALM_DOWN
        self.move = MOVE_SPEED       
        self.stop_horizontal = LOSE_IF_HORIZONTAL_COL
        self.clock = pygame.time.Clock()
        self.wall_stopped = False
        self.dir = os.path.dirname(__file__)
        self.dir_sounds = os.path.join(self.dir, 'sources/sounds/')
        self.dir_images = os.path.join(self.dir, 'sources/images/')
        self.font = pygame.font.match_font(FONT)
        self.difficulty  = DIFF_NORMAL
        self.getResult = False
 

    def start(self):
        self.menu()
        self.new()

    def generate_elements(self):
        #Plataforma
        self.platform = Platform()
        self.sprites = pygame.sprite.Group()#Agrupar diferentes sprites que se usarán en el juego: plataforma, personaje, monedas...
        self.sprites.add(self.platform)
        #Jugador
        self.player = Player(100, self.platform.rect.top-200, self.platform.rect.top, self.dir_images) #Lo colocamos en x 100 y en la parte más alta de la plataforma. - Se hace que caiga de una altura de 200
        self.sprites.add(self.player)
        #Obstáculo
        self.walls = pygame.sprite.Group()
        #Monedas/Gotas/Etc
        self.drops = pygame.sprite.Group() 
        self.generateWalls()
        pygame.mixer.music.load(os.path.join(self.dir_sounds, 'bensound-creativeminds.mp3'))
        pygame.mixer.music.set_volume(0.25) #float 0.0 - 1.0
        pygame.mixer.music.play(-1, 0.0) 
    
    def generateWalls(self):
        last_position = WIDTH+100
        if not len(self.walls)>0:
            for w in range(0,MAX_WALLS):
                left = random.randrange(last_position+200, last_position+400)
                wall = Wall(40,  random.randrange(100, 300), RED, left,  self.platform.rect.top, self.dir_images)
                last_position = wall.rect.right
                self.sprites.add(wall)
                self.walls.add(wall)
            self.level +=1
            if self.level > LVL_MAX:
                self.playing = False
            self.generateDrops()


    def generateDrops(self):
        last_position = WIDTH+100
        for c in range(0,MAX_DROPS):
            pos_x = random.randrange(last_position +180, last_position+300)
            drop = Drop(pos_x, 100, self.dir_images)
            last_position = drop.rect.right
            self.sprites.add(drop)
            self.drops.add(drop)

    def new(self):
        self.score = 0
        self.level = 0
        self.playing = True
        self.background = pygame.image.load(os.path.join(self.dir_images, 'background.jpg'))
        self.background =  pygame.transform.scale(self.background , (WIDTH, HEIGHT)) 
        self.generate_elements()
        self.run()

    def run(self):
        while(self.running):
            self.clock.tick(CALM_DOWN)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Cuando se hace click en el botón cerrar
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.player.jump()

        if key[pygame.K_r] and not self.playing:
            self.new()

    def draw(self):
        # self.surface.fill(WHITE)
        self.surface.blit(self.background, (0,0))
        self.draw_score()
        self.draw_level()     
        self.draw_result()
        self.showDifficulty()
        self.sprites.draw(self.surface)
        pygame.display.flip()#ACTUALIZA LA PANTALLA, SE HARÁ SOBRE TODA LA SUPERFICIE.


    def update(self):
        if self.playing:
            wall = self.player.collide_with(self.walls)
            if wall:
                if self.player.collide_bottom(wall):
                    if self.wall_stopped:
                        self.reestartmove()
                    self.player.skid(wall)  
                else:
                    if not pygame.mixer.get_busy():
                        sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'collision.wav'))
                        sound.play()
                    self.stop()                  
            else:
                if not self.stop_horizontal:
                    self.reestartmove()

            drop = self.player.collide_with(self.drops)
            if drop:
                self.score += 1
                drop.kill()
                sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'coin.wav'))
                sound.play()

            self.sprites.update()
            self.player.validate_platform(self.platform)
            self.updateElements(self.walls)
            self.updateElements(self.drops)
            self.generateWalls()       

    
    def stop(self):
        if not self.playing:
            self.player.stop()
            self.stopelements(self.walls)
            self.stopelements(self.drops)
        if self.stop_horizontal:
            self.player.stop()
            self.stopelements(self.walls)
            self.stopelements(self.drops)
            self.playing = False
        else:
            self.stopelements(self.walls)
            self.stopelements(self.drops)



    def stopelements(self, elements):
        self.wall_stopped = True
        for element in elements:
            element.stop()

    
    def reestartmove(self):
        self.returnMoveElements(self.walls)
        self.returnMoveElements(self.drops)
    
    def returnMoveElements(self, elements):
        self.wall_stopped = False
        for element in elements:
            element.restart()

    def updateElements(self, elements):
        for element in elements:
            if not element.rect.right >0: #No visible
                element.kill()#Pium pium
    
    def draw_score(self):
        self.display_text(f"Score: {self.score}", 25, WHITE, WIDTH//2, 30)

    def display_text(self, text, size, color, pos_x, pos_y, position=1):        
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        rect = text.get_rect()
        if position == 1:
            rect.midtop = (pos_x, pos_y)
        elif position == 2:
            rect.topleft = (pos_x, pos_y)
        else:
            rect.topright = (pos_x, pos_y)
        self.surface.blit(text, rect)
    

        
    def draw_level(self):
        self.display_text(f"Level: {self.level}", 25, WHITE, 0, 30, 2)

    def draw_result(self):
        if not self.playing:
            if(pygame.mixer.music.get_busy()==True):
                pygame.mixer.music.fadeout(5000)
            drops = (self.level)*MAX_DROPS//2
            win_condition = drops *  self.difficulty
            if self.score >= win_condition:
                if not pygame.mixer.get_busy() and not self.getResult:
                        self.getResult = True
                        sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'won.wav'))
                        sound.play()
                text = f"Has ganado, has conseguido {self.score} de {drops}"
             
            else:
                if not pygame.mixer.get_busy() and not self.getResult:
                        self.getResult = True
                        sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'lose.wav'))
                        sound.play()
                text = f"Has perdido, has conseguido {self.score} de {drops}"

            self.display_text(text, 60, RED, WIDTH//2, HEIGHT//2-35)
            text = "Presiona r para volver a jugar"
            self.display_text(text, 50, RED, WIDTH//2, HEIGHT//2+35)

    def showDifficulty(self):
        if self.difficulty == DIFF_EASY:
            diff = "Easy"
        elif self.difficulty == DIFF_NORMAL:
            diff = "Normal"
        elif self.difficulty == DIFF_HARD:
            diff = "Hard"
        elif self.difficulty == DIFF_MASTER:
            diff = "Master"
        else:
            diff = "Wow."
        self.display_text(f"{diff}  ", 20, WHITE, WIDTH, 30, 3)

    def menu(self):
        self.surface.fill(BLACK)
        self.display_text('Presiona una tecla para comenzar', 20, WHITE, WIDTH//2, HEIGHT//2)
        pygame.display.flip()
        self.waitMenu()
    
    def waitMenu(self):
        wait  = True
        while wait:
            self.clock.tick(CALM_DOWN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    wait = False
                
