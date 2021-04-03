import pygame
import sys

pygame.init()#Para inicializarlo

#1. Creación y modificación de ventana.
width =  400#px
height =  500
surface = pygame.display.set_mode((width, height))#Para crear ventana. Retorna un objeto surface. - La surface inicial con la que se trabajará
pygame.display.set_caption("Shogame❤py") #Set cabecera de ventana.

#colors - Establecemos algunos colores con el objecto pygame.Color
#RGB - Red greeb blue (0-255)
orange = pygame.Color(255,140,0)
red = pygame.Color(255,0,0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 48)
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Cuando se hace click en el botón cerrar
            pygame.quit()
            sys.exit()
        
        #Mouse event
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("Click "+str(event))
            print(event.pos)
            if event.button == 1:
                print("Left")
            if event.button == 2:
                print("Center")
            if event.button == 3:
                print("Right")
            if event.button == 4:
                print("Scroll up")
            if event.button == 5:
                print("Scroll down")

        if event.type == pygame.MOUSEBUTTONUP:
            # print("Not clicki")
            pass
    
    pos_x, pos_y = pygame.mouse.get_pos() #tupla x y

    message = f"x: {pos_x}, y: {pos_y}"
    text = font.render(message, True, black)
    rc = text.get_rect()
    rc.center = (width//2, height//2)


    surface.fill(orange)
    surface.blit(text,rc)
    #Actualizar pantalla
    pygame.display.update()       