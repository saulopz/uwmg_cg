import pygame
from vector2d import Vector2D, grad2radians, radians2grad

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

v0 = Vector2D(100, 50)
v1 = Vector2D(300, 45)
v2 = Vector2D(0, 100)

print("Ângulo entre v1 e v2:", radians2grad(v1.angle_between(v2)), "graus")


running = True
while running:
    screen.fill((255, 255, 255))  # fundo branco

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    v0.show(screen, color=(255, 0, 0), origin=(400, 300), scale=1.0)
    v1.show(screen, color=(0, 255, 0), origin=(400, 300), scale=1.0)
    v2.show(screen, color=(0, 0, 255), origin=(400, 300), scale=1.0)

    v0.rotate(grad2radians(-1))
    v1.rotate(grad2radians(-0.1))
    v2.rotate(grad2radians(-0.5))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
