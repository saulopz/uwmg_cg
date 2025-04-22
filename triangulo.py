import sys
import pygame


class Point:
    def __init__(self, x: float, y: float):     # Nosso constructor do Ponto
        self.x: float = x                       # Inicializamos o x
        self.y: float = y                       # Inicializamos o y


screen = pygame.display.set_mode((800, 600))    # Inicializamos o pygame
triangle: list[Point] = [                       # Criamos nosso triângulo
    Point(50, 100),                             # Primeiro ponto
    Point(100, 50),                             # Segundo ponto
    Point(150, 100)                             # Terceiro ponto
]
while True:                                     # Iniciamos o laço do gameloop
    for event in pygame.event.get():            # Testamos os eventos
        if event.type == pygame.QUIT:           # Se for o evento QUIT (botão x da janela)
            sys.exit(0)                         # Fechamos o programa
        elif event.type == pygame.KEYDOWN:      # Se uma tecla for pressionada
            if event.key == pygame.K_ESCAPE:    # E essa tecla for ESC
                sys.exit(0)                     # Fechamos o programa

    screen.fill((255, 255, 255))                # Pintamos o fundo de branco

    pygame.draw.line(screen, (0, 0, 0),         # Criamos nossa primeira linha
        (triangle[0].x, triangle[0].y),         # conectando o ponto 0
        (triangle[1].x, triangle[1].y))         # com o ponto 1
    pygame.draw.line(screen, (0, 0, 0),         # Criamos nossa segunda linha
        (triangle[1].x, triangle[1].y),         # conectando o ponto 1
        (triangle[2].x, triangle[2].y))         # ao ponto 2
    pygame.draw.line(screen, (0, 0, 0),         # Criamos nossa terceira linha
        (triangle[2].x, triangle[2].y),         # conectando o ponto 2
        (triangle[0].x, triangle[0].y))         # ao ponto 0

    pygame.display.flip()                       # Trocamos a página de desenho

pygame.quit()                                   # Finaliza o pygame
