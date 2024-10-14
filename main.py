from constantes import ALTO, ANCHO, Mover_arriba, Mover_abajo, Mover_derecha, Mover_izquierda, colorBg,FPS
from personajes import Personaje
import pygame

pygame.init()

# Poner nombre a la ventana
pygame.display.set_caption("Nuevo juego")
ventana = pygame.display.set_mode((ALTO, ANCHO))

# Se instancia al jugador
Jugador = Personaje(50, 50)
reloj=pygame.time.Clock()


run = True
while run:
    reloj.tick(FPS)
    

    ventana.fill(colorBg)

    delta_x = 0
    delta_y = 0 

    # Aquí se deben verificar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_a:
                Mover_izquierda = True
            if event.key == pygame.K_d:
                Mover_derecha = True    
            if event.key == pygame.K_w:
                Mover_arriba = True    
            if event.key == pygame.K_s:
                Mover_abajo = True
        if event.type == pygame.KEYUP:  # Para manejar el levantamiento de teclas
            if event.key == pygame.K_a:
                Mover_izquierda = False
            if event.key == pygame.K_d:
                Mover_derecha = False    
            if event.key == pygame.K_w:
                Mover_arriba = False    
            if event.key == pygame.K_s:
                Mover_abajo = False

    # Movimiento del jugador
    if Mover_arriba:
        delta_y = -5
    if Mover_abajo:
        delta_y = 5
    if Mover_derecha:
        delta_x = 5   
    if Mover_izquierda:
        delta_x = -5 

    Jugador.mover(delta_x, delta_y)
    Jugador.dibujar(ventana)

    pygame.display.update()

pygame.quit()
