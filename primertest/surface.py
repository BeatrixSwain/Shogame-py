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

#Generar colores por tuplas
my_color = (255,140,0) #RGB


#[+] RECTÁNGULOS
#Definición de los rectángulos
x = 50
y = 50
ojito_izq = pygame.Rect(x, y, 100, 100) #x, y, width, height
ojito_dcha = pygame.Rect(x+200, y, 100, 100) #x, y, width, height
boquita = pygame.Rect(x, y+200, 300, 20) #x, y, width, height
#generar rectánculo por tupla 
# cubito = (x, y, 50, 50)#x, y, width, height.
cubito = pygame.Rect(x, y, 50, 50) #x, y, width, height
cubito.center = (width//2, height//2) #Se refiere al centro del cubo, con los parámetros se obtiene el centro de la pantalla creada porque son los parámetros anteriores.
cubito2 = pygame.Rect(0, 0, 50, 50) 

#Obtener las coordenadas de cubito.
print(cubito.x)
print(cubito.y)

####
#[+] Nueva superficie
surface2 = pygame.Surface((200,200))#Definir las dimensiones de la superficie
surface2.fill(white) #Para pintarla
rect = surface2.get_rect() #Todas las surfaces tienen un rect, lo obtenemos.
rect.center = (width//2, height//2) #Se setean las coordenadas según su centro.

#Pintar una imagen
#cargarla
beatrix = pygame.image.load('images/doll.png') # -> retornará una superficie 
# New width and height will be (50, 30).
beatrix_small = pygame.transform.scale(beatrix, (200, 200)) #Setear el tamaño, porque la imagen era muy grande :D
rectbeat = beatrix_small.get_rect() #Todas las surfaces tienen un rect, lo obtenemos.
rectbeat.center = (width//2, height//2) #Se centra
#Obtener fuente
font = pygame.font.Font('freesansbold.ttf', 20) #Esta fuente viene con pygame, tamaño
#Se puede añadir una fuente guardada, simplemente hay que poner la path.
#Crear texto
message = font.render('Hola, ¿Cómo te llamas?', True, black) #texto, ?, color # -> retorna superficie
msgc = message.get_rect() #Todas las surfaces tienen un rect, lo obtenemos.
msgc.center = (width//2, height//2) #Se centra

font2 = pygame.font.Font('freesansbold.ttf', 14)

#cargar canción
pygame.mixer.music.load('sounds/bensound-creativeminds.mp3')
#Configurar volumen
pygame.mixer.music.set_volume(0.25) #float 0.0 - 1.0
#Reproducirla:
pygame.mixer.music.play(-1, 0.0) #puede recibir dos argumentos de forma opcional.  cuantas veces se quiere que se reproduzca de forma consecutiva, momento de comenzar de la cación (2, 1.30)  que se reproduzca dos veces, a partir del minuto 1.30 - Si queremos que se repita continuamente, se establece con -1
# pygame.mixer.music.rewind() #Reiniciar la canción
# pygame.mixer.music.pause() #Pausarla
# pygame.mixer.music.stop()#detenerla
# pyagem.mixer.music.fadeout(5000)#Va reduciendo poco a poco. Recibe el número de milisegundos que tomará para irse deteniendose.

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Cuando se hace click en el botón cerrar
            pygame.quit()
            sys.exit()
    
    surface.fill(my_color)#pintar la pantalla de ese color
    #Mostrar cubitos
    # pygame.draw.rect(surface, white, ojito_izq)#Sobre qué superficie se pintará, de qué color el rectángulo, el rectangulo
    # pygame.draw.rect(surface, white, ojito_dcha)#Sobre qué superficie se pintará, de qué color el rectángulo, el rectangulo
    # pygame.draw.rect(surface, red, boquita)#Sobre qué superficie se pintará, de qué color el rectángulo, el rectangulo
    # pygame.draw.rect(surface, black, cubito)#Sobre qué superficie se pintará, de qué color el rectángulo, el rectangulo
    #[+] Pintar otras figuras.
    # pygame.draw.circle(surface, blue, (200,400), 25)#superficie, color, (x coordenada centro circulo, y coordenadas centro circulo), radio px
    # pygame.draw.line(surface, black, (0,0), (200, 200), 2) #superficie, color, punto A, punto B, grosor

    #[+]Dibujar polígonos.
    #Triángulo
    # pygame.draw.polygon(surface, black, ((0, 400),(100, 300),(200,400)))
    # #Pentágono
    # pygame.draw.polygon(surface, red, (
    #     (146,0),
    #     (291,106),
    #     (236,277),
    #     (56,277),
    #     (0,106) 
    # ))

    # #Añadimos la surface2 a la 1 - 
    # surface.blit(surface2, rect)#Superficie, posición x y en la que se va  a pintar - Se coloca en el centro.
    # pygame.draw.rect(surface2, black, cubito2) #Se dibujac cubito2 en la nueva superficie.

    #Cargamos la imagen.
    surface.blit(beatrix_small, rectbeat)
  
    s = pygame.time.get_ticks()//1000 #Milisegundos

    if s <=3:
        surface.blit(message, (msgc.x, 100) )
    elif s>3 and s<=5:
        txt = font.render("...", True, black)
        rt = txt.get_rect()
        rt.center = (width//2, height//2)
        surface.blit(txt,(rt.x,100))
    elif s>5 and s<=9:
        txt = font.render("Yo soy Beatrix, encantada!", True, black)
        rt = txt.get_rect()
        rt.center = (width//2, height//2)
        surface.blit(txt,(rt.x,100))
    elif s>9 and s<=12:
        txt = font.render("¿Sabes dónde estamos?", True, black)
        rt = txt.get_rect()
        rt.center = (width//2, height//2)
        surface.blit(txt,(rt.x,100))
    else:
        txt = font.render("Me siento extraña...", True, black)
        rt = txt.get_rect()
        rt.center = (width//2, height//2)
        surface.blit(txt,(rt.x,100))
        if(pygame.mixer.music.get_busy()==True):
            pygame.mixer.music.fadeout(5000)

    text = font2.render(f"{s} s", True, red)
    surface.blit(text,(5,5))
    

    #Actualizar pantalla
    pygame.display.update()