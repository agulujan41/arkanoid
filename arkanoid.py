import pygame

#creamos ventana
color_fondo = (200,255,255)
ventana = pygame.display.set_mode((500,500))
ventana.fill(color_fondo)
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()


AMARILLO = (255,255,0)
AZUL_OSCURO = (0,0,100)
AZUL = (80,80,255)
NEGRO = (0,0,0)
VERDE = (0,255,0)
ROJO = (255,0,0)


gameover=False

class Rectangulo():
    def __init__(self,x,y,ancho,alto):
        self.rect = pygame.Rect(x,y,ancho,alto)
        self.color_relleno = color_fondo

    def color(self,nuevoColor):
        self.color_relleno = nuevoColor
    
    def rellenar(self):
        pygame.draw.rect(ventana,self.color_relleno,self.rect)
    #puntos
    def estaTocandoRectangulo(self,x,y):
        return self.rect.collidepoint(x,y)
    #rectangulos
    def estaChocandoRectangulo(self,otroRectangulo):
        return self.rect.colliderect(otroRectangulo)

class Imagen(Rectangulo):
    def __init__(self,nombreArchivo, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)
        self.imagen = pygame.image.load(nombreArchivo)
    def dibujar(self):
        ventana.blit(self.imagen,(self.rect.x,self.rect.y))


enemigos = []
comienzo_x = 5
comienzo_y = 5
y = comienzo_y
x = comienzo_x
cantidad_enemigos = 9
for i in range(3):
    x = comienzo_x + (i*27.5)
    for j in range(cantidad_enemigos):
        enemigo = Imagen("enemigo.png",x,y,50,50)
        enemigos.append(enemigo)
        x = x+55
    y = y + 55
    cantidad_enemigos = cantidad_enemigos -1
pelota = Imagen("pelota.png",230,230,50,50)


plataforma_x = 200
plataforma_y = 330
movimientoDerecha = False
movimientoIzquierda = False
plataforma = Imagen("plataforma.png",plataforma_x,plataforma_y,100,30)

aumentarPelotaX = 5
aumentarPelotaY = 5

while not gameover:
    plataforma.rellenar()
    pelota.rellenar()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gameover = True
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                movimientoDerecha = True
            if event.key == pygame.K_LEFT:
                movimientoIzquierda = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                movimientoDerecha = False
            if event.key == pygame.K_LEFT:
                movimientoIzquierda = False
    

    if movimientoDerecha:
        plataforma.rect.x += 5
    if movimientoIzquierda:
        plataforma.rect.x -= 5
    


    pelota.rect.x+= aumentarPelotaX
    pelota.rect.y+= aumentarPelotaY 

    #pelota no se pase de la pantalla
    if pelota.rect.y < 0:
           aumentarPelotaY*= -1
    if pelota.rect.y > 450:
           aumentarPelotaY*= -1
    if pelota.rect.x < 0:
           aumentarPelotaX*= -1
    if pelota.rect.x > 450:
           aumentarPelotaX*= -1
    
    if pelota.estaChocandoRectangulo(plataforma.rect):
        aumentarPelotaY*=-1
    for enemigo in enemigos:
        enemigo.dibujar()
    pelota.dibujar()
    plataforma.dibujar()
    pygame.display.update()

    clock.tick(40)