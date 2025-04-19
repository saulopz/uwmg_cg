import pygame
import copy
from math import sin, cos, radians

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw(tela, figura, cor):
    size = len(figura)
    for i in range(size):
        j = i + 1
        if j >= size:
            j = 0
        pygame.draw.line(tela, cor,
            (figura[i].x, figura[i].y),
            (figura[j].x, figura[j].y), 1)

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Triângulo")

triangulo = [
    Ponto(200, 250),
    Ponto(300, 150),
    Ponto(400, 250)
]

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill((255, 255, 255))  # Fundo branco
    draw(tela, triangulo, (255, 0, 0))
    pygame.display.flip()
pygame.quit()
