import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 7
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Game objects
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
paddle1 = pygame.Rect(20, HEIGHT//2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH - 30, HEIGHT//2 - 60, 10, 120)

ball_dx, ball_dy = random.choice([BALL_SPEED, -BALL_SPEED]), random.choice([BALL_SPEED, -BALL_SPEED])

# Scoring
score1 = 0
score2 = 0

# Function to make AI easier
def easy_ai_move():
    # Only move if the ball is near the paddle (not constantly)
    if abs(paddle2.centery - ball.centery) < 100:
        if paddle2.centery < ball.centery and paddle2.bottom < HEIGHT:
            paddle2.y += PADDLE_SPEED // 2  # Slow down AI movement
        if paddle2.centery > ball.centery and paddle2.top > 0:
            paddle2.y -= PADDLE_SPEED // 2  # Slow down AI movement

# Main loop
running = True
while running:
    pygame.time.delay(15)
    screen.fill((0, 0, 0))
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement for Player 1 (controlled by the user)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    
    # Easy AI for Player 2
    easy_ai_move()

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy
    
    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx = -ball_dx
    
    # Update score if ball goes out of bounds
    if ball.left <= 0:
        score2 += 1  # Player 2 scores
        ball.x, ball.y = WIDTH//2 - 15, HEIGHT//2 - 15
        ball_dx = random.choice([BALL_SPEED, -BALL_SPEED])
        ball_dy = random.choice([BALL_SPEED, -BALL_SPEED])
    
    if ball.right >= WIDTH:
        score1 += 1  # Player 1 scores
        ball.x, ball.y = WIDTH//2 - 15, HEIGHT//2 - 15
        ball_dx = random.choice([BALL_SPEED, -BALL_SPEED])
        ball_dy = random.choice([BALL_SPEED, -BALL_SPEED])
    
    # Draw everything
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    
    # Display the scores
    score_text = FONT.render(f"{score1}  -  {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))
    
    pygame.display.update()

pygame.quit()

