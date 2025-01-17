import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
#width, height = 600, 400
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_block = 10
snake_speed = 10
snake_body = []
snake_length = 1

# Initial position of the snake
x, y = width // 2, height // 2
x_change, y_change = 0, 0

# Food properties
food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Set the game clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Function to display score
def display_score(score):
    value = font.render(f"Score: {score}", True, white)
    window.blit(value, [0, 0])

# Main game loop
game_over = False
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change == 0:
                x_change, y_change = -snake_block, 0
            elif event.key == pygame.K_RIGHT and x_change == 0:
                x_change, y_change = snake_block, 0
            elif event.key == pygame.K_UP and y_change == 0:
                x_change, y_change = 0, -snake_block
            elif event.key == pygame.K_DOWN and y_change == 0:
                x_change, y_change = 0, snake_block

    # Update the snake's position
    x += x_change
    y += y_change

    # Wrap around the screen
    if x >= width:
        x = 0  # Move to the left side
    elif x < 0:
        x = width - snake_block  # Move to the right side
    if y >= height:
        y = 0  # Move to the top
    elif y < 0:
        y = height - snake_block  # Move to the bottom

    # Draw background, snake, and food
    window.fill(black)
    pygame.draw.rect(window, red, [food_x, food_y, snake_block, snake_block])

    # Update the snake's body
    snake_head = [x, y]
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check for self-collision
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(window, green, [segment[0], segment[1], snake_block, snake_block])

    # Check if snake has eaten the food
    if x == food_x and y == food_y:
        food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake_length += 1

    # Display score
    display_score(snake_length - 1)

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
quit()
