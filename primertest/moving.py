import pygame
import sys

pygame.init()#Para inicializarlo

calm_down = 2
move = 1
#1. Creación y modificación de ventana.
width =  400#px
height =  500
surface = pygame.display.set_mode((width, height))#Para crear ventana. Retorna un objeto surface. - La surface inicial con la que se trabajará
pygame.display.set_caption("Shogame❤py") #Set cabecera de ventana.

#RGB - Red greeb blue (0-255)
orange = pygame.Color(255,140,0)
red = pygame.Color(255,0,0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

#Image
#Little Beatrix
beatrix = pygame.image.load('images/doll.png') # -> retornará una superficie 
beatrix_small = pygame.transform.scale(beatrix, (50, 50)) #Set size
rectbeat = beatrix_small.get_rect() 
rectbeat.center = (width//2, height//2) #Center it
mask_beatrix = pygame.mask.from_surface(beatrix_small) #Para detectar bien las colisiones con imagenes con transparencias, se genera una mask


#Block
# rect1 = pygame.Rect(0,0, 100, 80)
surfacerect1 =  pygame.Surface((100, 80))
# surfacerect1 =  pygame.image.load('images/heart.png')
# surfacerect1 = pygame.transform.scale(surfacerect1, (100, 100)) #Set size
surfacerect1.fill(black)
rect1 = surfacerect1.get_rect()
rect1.center = (width//2, height//2) #Center it
mask_rect1 = pygame.mask.from_surface(surfacerect1)

#Aprender a mostrar el rectángulo de una imagen:
surface2 =  pygame.Surface((rectbeat.width, rectbeat.height), pygame.SRCALPHA) #Trabajar con transparencias. Creates an empty per-pixel alpha Surface -> a type of transparency
surface2.fill((0,0,0,50)) #(4)El alpha, la transparencia
rect2 = surface2.get_rect()
rect2.center = rectbeat.center
#Font
font = pygame.font.Font('freesansbold.ttf', 48)

while True: 
    pygame.time.delay(calm_down)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Cuando se hace click en el botón cerrar
            pygame.quit()
            sys.exit()
    
    surface.fill(orange)

    #Moving with mouse
    pos_x, pos_y = pygame.mouse.get_pos()
    if pos_x!=0 and pos_y != 0:
        rectbeat.center = (pos_x, pos_y)
        rect2.center = rectbeat.center

    #Moving with keyboard.
    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
    #     rectbeat.x -= move
    # if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
    #     rectbeat.x += move
    # if pressed[pygame.K_w] or pressed[pygame.K_UP]:
    #     rectbeat.y -= move
    # if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
    #     rectbeat.y += move

    # #Validation pos
    # if rectbeat.left < 0:
    #     rectbeat.left = 0    
    # if rectbeat.right > width:
    #     rectbeat.right = width
    # if rectbeat.top < 0:
    #     rectbeat.top = 0
    # if rectbeat.bottom > height:
    #     rectbeat.bottom = height

    ####
    surface.blit(surface2, rect2)
    surface.blit(beatrix_small, rectbeat)

    #Rectángulo
    # pygame.draw.rect(surface, black, rect1)
    surface.blit(surfacerect1, rect1)


    #Colisiones

    offset = (rect1.x-rectbeat.x, rect1.y-rectbeat.y) #Almacena una coordenada de intersección 
    #- El orden es importante. Va primero el rectángulo del que no se compara la máscara que está abajo. 
    # Es decir, compramos la máscara de beatrix así que va primero la máscara del rectángulo.
    # if rect1.colliderect(rectbeat): #Colisión normal sin tener en cuenta la transparencia.
    if mask_beatrix.overlap(mask_rect1, offset):
        if(pygame.mixer.get_busy()!=True):
            sound = pygame.mixer.Sound('sounds/collision.wav')
            sound.play()
        text = font.render("¿Dónde toi?", True, red)
        rect3 = text.get_rect()
        rect3.midtop = (width//2, 50)
        surface.blit(text, rect3)
        # print("Ouch!")
    #Actualizar pantalla.
    pygame.display.update()       

