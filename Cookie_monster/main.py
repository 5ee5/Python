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
monsterX = 350
monsterY = 350
monsterX_change = 0
monsterY_change = 0

cookie = pygame.image.load('Python/Cookie_monster/assets/cookie.png')

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                monsterX_change = 2.5
                monsterY_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                monsterX_change = -2.5
                monsterY_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                monsterX_change = 0
                monsterY_change = -2.5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                monsterX_change = 0
                monsterY_change = 2.5


    monsterX += monsterX_change
    monsterY += monsterY_change

    if monsterX < 0:
        monsterX = 0
    elif monsterY < 0:
        monsterY = 0
    if monsterX > 735:
        monsterX = 735
    elif monsterX > 635:
        monsterY = 635
    
    window.blit(monster, (monsterX, monsterY))
    window.fill('#00ffff')
    window.blit(monster, (monsterX, monsterY))

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
sys.exit()
