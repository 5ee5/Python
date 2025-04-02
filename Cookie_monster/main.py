import pygame
import sys
import random

pygame.init()
windowX = 800
windowY = 700

window = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption("Cookie Monster")

icon = pygame.image.load('Python/Cookie_monster/assets/cookie.png')
pygame.display.set_icon(icon)

background = pygame.image.load('Python/Cookie_monster/assets/underground.png')
background = pygame.transform.scale(background, (windowX, windowY))
monster = pygame.image.load('Python/Cookie_monster/assets/monster.png')
monsterX = 350
monsterY = 350
monsterX_change = 0
monsterY_change = 0

cookie = pygame.image.load('Python/Cookie_monster/assets/cookie.png')
cookie = pygame.transform.scale(cookie, (50, 50))
cookieX = random.randint(0, 636)
cookieY = random.randint(0, 436)
cookie_is_eaten = False

while not cookie_is_eaten:

    def cookie_is_eaten(monsterX, monsterY, cookieX, cookieY):
        distance = ((monsterX - cookieX) ** 2 + (monsterY - cookieY) ** 2) ** 0.5
        if distance <= 48:
            return True
        return False

clock = pygame.time.Clock()

bg_x = (windowX - background.get_width()) // 2
bg_y = (windowY - background.get_height()) // 2

running = True
while running:
    window.blit(background, (bg_x, bg_y))
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
    elif monsterY > 635:
        monsterY = 635

    if cookie_is_eaten(monsterX, monsterY, cookieX, cookieY):
        cookieX = random.randint(0, 636)
        cookieY = random.randint(0, 436)        
    
    window.blit(monster, (monsterX, monsterY))
    window.blit(cookie, (cookieX, cookieY))
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
sys.exit()
