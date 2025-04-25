import pygame
import sys
import random

# Initialize Pygame
pygame.init()
windowX = 800
windowY = 700

window = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption("Cookie Monster")

# Load assets
icon = pygame.image.load('assets/cookie.png')
pygame.display.set_icon(icon)

cookie_sound = pygame.mixer.Sound('assets/cookie_sound.mp3')
cookie_sound.set_volume(1)

background = pygame.image.load('assets/underground.png')
background = pygame.transform.scale(background, (windowX, windowY))

monster = pygame.image.load('assets/monster.png')
monsterX = 350
monsterY = 350
monsterX_change = 0
monsterY_change = 0

score = 0

cookie_img = pygame.image.load('assets/cookie.png')
cookie_img = pygame.transform.scale(cookie_img, (50, 50))

# Generate cookies
num_cookies = 5
cookies = []
for _ in range(num_cookies):
    cookieX = random.randint(0, 750 - 50)
    cookieY = random.randint(0, 650 - 50)
    cookies.append({'img': cookie_img, 'x': cookieX, 'y': cookieY})

font = pygame.font.Font(None, 36)
start_ticks = pygame.time.get_ticks()
clock = pygame.time.Clock()

# Collision detection
def cookie_is_eaten(monsterX, monsterY, cookieX, cookieY):
    distance = ((monsterX - cookieX)**2 + (monsterY - cookieY)**2)**0.5
    return distance <= 48
    cookie_sound.play()

pygame.mixer.music.load('assets/Background_Music.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


# Main game loop
running = True
while running:
    window.blit(background, (0, 0))

    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    countdown = max(0, 30 - int(seconds_passed))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                monsterX_change = 2.5
                monsterY_change = 0
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                monsterX_change = -2.5
                monsterY_change = 0
            if event.key in [pygame.K_UP, pygame.K_w]:
                monsterX_change = 0
                monsterY_change = -2.5
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                monsterX_change = 0
                monsterY_change = 2.5

    monsterX += monsterX_change
    monsterY += monsterY_change

    # Boundary checking
    if monsterX < 0:
        monsterX = 0
    elif monsterY < 0:
        monsterY = 0
    if monsterX > 735:
        monsterX = 735
    elif monsterY > 635:
        monsterY = 635

    # Check for cookie collisions
    for i, cookie in enumerate(cookies):
        if cookie_is_eaten(monsterX, monsterY, cookie['x'], cookie['y']):
            score += 1
            cookies[i] = {
                'img': cookie_img,
                'x': random.randint(0, 750 - 50),
                'y': random.randint(0, 650 - 50)
            }

    window.blit(monster, (monsterX, monsterY))
    for cookie in cookies:
        window.blit(cookie['img'], (cookie['x'], cookie['y']))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    if countdown == 0:
        time_text = font.render("Time's up!", True, (255, 0, 0))
        window.blit(score_text, (10, 10))
        window.blit(time_text, (10, 50))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False
    else:
        time_text = font.render(f"Time: {countdown}", True, (255, 255, 255))
        window.blit(score_text, (10, 10))
        window.blit(time_text, (10, 50))
        pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
