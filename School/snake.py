import pygame
import random

pygame.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode([500, 500])
pygame.display.set_caption("elchin snake 2.v.0")


class Snake:

    def __init__(self, x, y):
        self.length = 1
        self.x_change = 0
        self.y_change = 0
        self.rectangles = []
        self.rectangles.append(pygame.Rect(x, y, 20, 20))

    def move(self):
        x = self.rectangles[-1].left
        y = self.rectangles[-1].top

        self.rectangles.append(
            pygame.Rect(x + self.x_change, y + self.y_change,
                        20, 20)
        )

        if len(self.rectangles) > self.length:
            self.rectangles.pop(0)

    def is_out_of_bounds(self, window):
        window_rect = window.get_rect()
        return not window_rect.contains(self.rectangles[-1])
    
    def is_crossing_itself(self):
        if snake.rectangles[-1].collidelist(snake.rectangles[:-1]) == -1:
            return False
        
        return True

    def draw(self, window):
        for rectangle in self.rectangles:
            pygame.draw.rect(window, [13, 55, 13], rectangle)

class Apple:
     
    size = 15

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def is_eaten(self, snake):
        apple_rect = pygame.Rect(
            self.x, self.y,
            Apple.size, Apple.size
        )
        
        return apple_rect.colliderect(snake.rectangles[-1])

    def draw(self, window):
        apple_rect = pygame.Rect(
            self.x, self.y,
            Apple.size, Apple.size
        )
        
        pygame.draw.rect(window, [255, 0, 0], apple_rect)


snake = Snake(240, 240)

apples = []
for i in range(3):
    apples.append(Apple(random.randint(0, 485), random.randint(0, 485)))

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.x_change = 0
                snake.y_change = -20

            if event.key == pygame.K_a:
                snake.x_change = -20
                snake.y_change = 0

            if event.key == pygame.K_s:
                snake.x_change = 0
                snake.y_change = 20

            if event.key == pygame.K_d:
                snake.x_change = 20
                snake.y_change = 0

    snake.move()

    for apple in apples:
        if apple.is_eaten(snake):
            snake.length += 1
            apple.x = random.randint(0, 485)
            apple.y = random.randint(0, 485)

    if snake.is_out_of_bounds(window) or snake.is_crossing_itself():
        pygame.quit()

    window.fill([0, 0, 0])
    snake.draw(window)

    for apple in apples:
        apple.draw(window)
        
    pygame.display.update()

    clock.tick(10)