import pygame
import sys

pygame.init()

window = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Cookie Monster")

icon = pygame.image.load('Python/Cookie_monster/assets/cookie.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill('#00ffff')
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
sys.exit()
