import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Desenhamos uma linha na tela, do ponto (30, 50) ao ponto (180, 200)
    pygame.draw.line(screen, (255, 0, 0),
        (30, 50), (180, 200))

    # Desenhamos um poligono com base no vetor de pontos passado como parâmetro.
    pygame.draw.polygon(screen, (0, 0, 255),
        [(200, 100), (300, 50), (400, 100), (350, 200), (250, 200)])

    pygame.display.flip()
pygame.quit()