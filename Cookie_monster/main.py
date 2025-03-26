import pygame
import sys

pygame.init()
windowX = 800
windowY = 700

window = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption("Cookie Monster")

icon = pygame.image.load('Python/Cookie_monster/assets/cookie.png')
pygame.display.set_icon(icon)

monster = pygame.image.load('Python/Cookie_monster/assets/monster.png')
monsterx = 350
monstery = 350
monsterx_change = 0
monstery_change = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                monsterx_change = 2.5
                monstery_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                monsterx_change = -2.5
                monstery_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                monsterx_change = 0
                monstery_change = -2.5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                monsterx_change = 0
                monstery_change = 2.5


    monsterx += monsterx_change
    monstery += monstery_change
    window.blit(monster, (monsterx, monstery))
    window.fill('#00ffff')
    window.blit(monster, (monsterx, monstery))

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
sys.exit()
