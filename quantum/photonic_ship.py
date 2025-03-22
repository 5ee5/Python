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
    K_w,
    K_a,
    K_s,
    K_d,
    K_e,
    K_r,
    K_x,
    K_h,
    K_z,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640  # Double the original height

score = 0
quantum_mode = False
ship_state = "|0>"
last_gate_applied = ""
gate_display_timer = 0
GATE_DISPLAY_DURATION = 60  # Duration to display the gate text (in frames)

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
score_font = pygame.font.SysFont('Comic Sans MS', 30)

ship = pygame.sprite.Sprite()
ship.surf = pygame.Surface((60, 20))
ship.surf.fill((255, 255, 255))
ship.rect = ship.surf.get_rect()

ship_copy = None

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
    if not quantum_mode:
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            if ship.rect.top > 0 and (ship.rect.top > SCREEN_HEIGHT // 2 or ship.rect.bottom <= SCREEN_HEIGHT // 2):
                ship.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            if ship.rect.bottom < SCREEN_HEIGHT and (ship.rect.bottom < SCREEN_HEIGHT // 2 or ship.rect.top >= SCREEN_HEIGHT // 2):
                ship.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            ship.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            ship.rect.move_ip(5, 0)

        if ship.rect.left < 0:
            ship.rect.left = 0
        if ship.rect.right > SCREEN_WIDTH:
            ship.rect.right = SCREEN_WIDTH
        if ship.rect.top <= 0:
            ship.rect.top = 0
        if ship.rect.bottom >= SCREEN_HEIGHT:
            ship.rect.bottom = SCREEN_HEIGHT

def teleportShip():
    while True:
        new_x = random.randint(0, SCREEN_WIDTH - ship.rect.width)
        new_y = random.randint(0, SCREEN_HEIGHT - ship.rect.height)
        ship.rect.topleft = (new_x, new_y)
        if not pygame.sprite.spritecollideany(ship, enemies):
            break

def switchScreen():
    if not quantum_mode:
        if ship.rect.top < SCREEN_HEIGHT // 2:
            ship.rect.top += SCREEN_HEIGHT // 2
        else:
            ship.rect.top -= SCREEN_HEIGHT // 2

def getShipState():
    return ship_state

def applyHadamard():
    global ship_state, quantum_mode, ship_copy
    if ship_state == "|0>":
        ship_state = "|+>"
        quantum_mode = True
        ship_copy = pygame.sprite.Sprite()
        ship_copy.surf = pygame.Surface((60, 20))
        ship_copy.surf.fill((255, 255, 255))
        ship_copy.rect = ship.surf.get_rect()
        ship_copy.rect.topleft = (ship.rect.left, ship.rect.top + SCREEN_HEIGHT // 2)
        all_sprites.add(ship_copy)
    elif ship_state == "|1>":
        ship_state = "|->"
        quantum_mode = True
        ship_copy = pygame.sprite.Sprite()
        ship_copy.surf = pygame.Surface((60, 20))
        ship_copy.surf.fill((255, 255, 255))
        ship_copy.rect = ship.surf.get_rect()
        ship_copy.rect.topleft = (ship.rect.left, ship.rect.top - SCREEN_HEIGHT // 2)
        all_sprites.add(ship_copy)
    elif ship_state == "|+>":
        ship_state = "|0>"
        quantum_mode = False
        all_sprites.remove(ship_copy)
        ship_copy = None
    elif ship_state == "|->":
        ship_state = "|1>"
        quantum_mode = False
        all_sprites.remove(ship_copy)
        ship_copy = None

def moveEnemiesVertically(direction):
    for enemy in enemies:
        enemy.rect.move_ip(0, direction)
        if enemy.rect.top > SCREEN_HEIGHT:
            enemy.rect.bottom = 0
        elif enemy.rect.bottom < 0:
            enemy.rect.top = SCREEN_HEIGHT

def measureAndCollapse():
    global ship_state, quantum_mode, ship_copy
    if ship_state == "|+>":
        ship_state = "|0>"
        ship.rect.top -= SCREEN_HEIGHT // 2
    elif ship_state == "|->":
        ship_state = "|1>"
        ship.rect.top += SCREEN_HEIGHT // 2
    quantum_mode = False
    all_sprites.remove(ship_copy)
    ship_copy = None

def displayMessage(message):
    my_font = pygame.font.SysFont('Comic Sans MS', 48)
    text_surface = my_font.render(message, False, (255, 0, 0), (0, 0, 0))
    screen.blit(text_surface, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3))
    pygame.display.flip()
    pygame.time.wait(2000)

def renderText(text, position, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

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

    # Draw a line in the middle of the screen
    pygame.draw.line(screen, (255, 255, 255), (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))

    score += 1

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_ESCAPE]: running = False
    if not quantum_mode:
        updateShip(pressed_keys)
    else:
        if pressed_keys[K_UP]:
            moveEnemiesVertically(-5)
        if pressed_keys[K_DOWN]:
            moveEnemiesVertically(5)

    if pressed_keys[K_SPACE] or pressed_keys[K_e]:
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

    if pressed_keys[K_r]:
        teleportShip()

    if pressed_keys[K_x] and not quantum_mode:
        switchScreen()

    if pressed_keys[K_z] and quantum_mode:
        if ship_state == "|+>":
            ship_state = "|->"
        elif ship_state == "|->":
            ship_state = "|+>"

    if pressed_keys[K_h]:
        applyHadamard()

    # Randomly apply quantum gates
    random_gate = random.randint(0, 300)
    if random_gate in [100, 200] and not quantum_mode:
        switchScreen()
        last_gate_applied = "X"
        gate_display_timer = GATE_DISPLAY_DURATION
    elif random_gate in [50, 250] and quantum_mode:
        if ship_state == "|+>":
            ship_state = "|->"
        elif ship_state == "|->":
            ship_state = "|+>"
        last_gate_applied = "Z"
        gate_display_timer = GATE_DISPLAY_DURATION
    elif random_gate == 150:
        applyHadamard()
        last_gate_applied = "H"
        gate_display_timer = GATE_DISPLAY_DURATION

    bullets.update()

    for bullet in bullets:
        enemies_hit = pygame.sprite.spritecollide(bullet, enemies, True)
        if enemies_hit:
            bullet.kill()
            score += 10

    if quantum_mode and pygame.sprite.spritecollideany(ship_copy, enemies):
        measureAndCollapse()
        if pygame.sprite.spritecollideany(ship, enemies):
            ship.kill()
            running = False
            displayMessage("Main ship destroyed! Twin ship survived!")
        else:
            displayMessage("Twin ship destroyed! Main ship survived!")

    if pygame.sprite.spritecollideany(ship, enemies):
        if quantum_mode:
            measureAndCollapse()
            displayMessage("Main ship destroyed! Twin ship survived!")
            if ship_copy:
                ship, ship_copy = ship_copy, ship
                all_sprites.add(ship)
                quantum_mode = False
        else:
            ship.kill()
            running = False
            displayMessage("Game Over! Ship destroyed!")

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    ship_state = getShipState()
    state_surface = score_font.render(ship_state, True, (255, 255, 255))
    screen.blit(state_surface, (SCREEN_WIDTH - 70, 40 ))

    score_surface = score_font.render(str(score), False, (255, 255, 255))
    screen.blit(score_surface, (730, 10))

    if gate_display_timer > 0:
        renderText(f"Last Gate: {last_gate_applied}", (10, 10), score_font)
        gate_display_timer -= 1

    pygame.display.flip()
    if there_is_message: pygame.time.wait(2000)
    pygame.time.Clock().tick(30)