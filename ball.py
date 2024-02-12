import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Splitting Ball")

# Define colors
black = (0, 0, 0)
white = (105, 105, 105)

# Ball class
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = random.choice([-2, 2])  # Random initial direction along x-axis
        self.dy = random.choice([-2, 2])  # Random initial direction along y-axis

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Check collisions with walls
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.dx *= -1  # Reverse direction along x-axis

        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.dy *= -1  # Reverse direction along y-axis

    def split(self):
        new_balls = [Ball(self.x, self.y, self.radius), Ball(self.x, self.y, self.radius)]
        return new_balls

    def draw(self):
        pygame.draw.circle(screen, white, (int(self.x), int(self.y)), int(self.radius))

# Main loop
clock = pygame.time.Clock()
balls = [Ball(width // 2, height // 2, 20)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    for ball in balls:
        ball.move()
        ball.draw()

        # Check if the ball hits the wall, then split it into two
        if ball.x - ball.radius <= 0 or ball.x + ball.radius >= width or \
           ball.y - ball.radius <= 0 or ball.y + ball.radius >= height:
            balls.extend(ball.split())
            balls.remove(ball)

    pygame.display.flip()
    clock.tick(30)
