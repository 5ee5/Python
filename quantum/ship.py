import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_f,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 320

score = 0

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
score_font = pygame.font.SysFont('Comic Sans MS', 30)

ship = pygame.sprite.Sprite()
ship.surf = pygame.Surface((60, 20))
ship.surf.fill((255, 255, 255))
ship.rect = ship.surf.get_rect()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10, 5))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center=(x, y))

    def update(self):
        self.rect.move_ip(10, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

def updateShip(pressed_keys):
    if pressed_keys[K_UP]:
        ship.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        ship.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        ship.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        ship.rect.move_ip(5, 0)

    if ship.rect.left < 0:
        ship.rect.left = 0
    if ship.rect.right > SCREEN_WIDTH:
        ship.rect.right = SCREEN_WIDTH
    if ship.rect.top <= 0:
        ship.rect.top = 0
    if ship.rect.bottom >= SCREEN_HEIGHT:
        ship.rect.bottom = SCREEN_HEIGHT

CREATING_ENEMY_TIME_INTERVAL = 250
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, CREATING_ENEMY_TIME_INTERVAL)

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(ship)

def createEnemy():
    enemy = pygame.sprite.Sprite()
    enemy.surf = pygame.Surface((20, 10))
    enemy.surf.fill((255, 0, 0))
    enemy_X = random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)
    enemy_Y = random.randint(0, SCREEN_HEIGHT)
    enemy.rect = enemy.surf.get_rect(center=(enemy_X, enemy_Y))
    enemy.speed = random.randint(5, 20)
    enemies.add(enemy)
    all_sprites.add(enemy)

def updateEnemies():
    for enemy in enemies:
        enemy.rect.move_ip(-enemy.speed, 0)
        if enemy.rect.right < 0:
            enemy.kill()

there_is_message = False
enemies_paused = False
pause_timer = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY and not enemies_paused:
            createEnemy()
    screen.fill((0, 0, 0))

    score += 1

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_ESCAPE]: running = False
    updateShip(pressed_keys)

    if pressed_keys[K_SPACE]:
        bullet = Bullet(ship.rect.right, ship.rect.centery)
        bullets.add(bullet)
        all_sprites.add(bullet)

    if pressed_keys[K_f] and not enemies_paused:
        enemies_paused = True
        pause_timer = 60 

    if enemies_paused:
        pause_timer -= 1
        if pause_timer <= 0:
            enemies_paused = False
    else:
        updateEnemies()

    bullets.update()

    for bullet in bullets:
        enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)
        if enemies_hit:
            bullet.kill()
            score += 10

    if pygame.sprite.spritecollideany(ship, enemies):
        ship.kill()
        running = False
        my_font = pygame.font.SysFont('Comic Sans MS', 48)
        text_surface = my_font.render("Game Over! ", False, (255, 0, 0), (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3))
        there_is_message = True

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    score_surface = score_font.render(str(score), False, (255, 255, 255))
    screen.blit(score_surface, (730, 10))

    pygame.display.flip()
    if there_is_message: pygame.time.wait(2000)
    pygame.time.Clock().tick(30)