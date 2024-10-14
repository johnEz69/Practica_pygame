import pygame

class Personaje:
    def __init__(self, x, y):
        self.forma = pygame.Rect(x, y, 20, 20)  # Se usa pygame.Rect para definir el rectángulo del personaje
        self.color = (255, 0, 0)  # Color rojo para el personaje
        self.forma_x = x  # Posición inicial en x
        self.forma_y = y  # Posición inicial en y

    def mover(self, delta_x, delta_y):
        self.forma_x += delta_x  # Actualizar la posición en x
        self.forma_y += delta_y  # Actualizar la posición en y
        self.forma.topleft = (self.forma_x, self.forma_y)  # Actualizar la posición del rectángulo

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.forma)  # Dibujar el rectángulo en la ventana

