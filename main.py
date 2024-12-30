import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")

# Game variables
clock = pygame.time.Clock()
running = True

# Player variables
player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Falling objects variables
object_width, object_height = 50, 50
falling_objects = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Inside the game loop, add player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Draw the player
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))

    # Inside the game loop, add object spawning
    if random.randint(1, 20) == 1:  # Adjust the frequency of spawning
        object_x = random.randint(0, WIDTH - object_width)
        falling_objects.append([object_x, 0])  # Start at the top

    # Update falling objects
    for obj in falling_objects:
        obj[1] += 5  # Move down
        pygame.draw.rect(screen, (255, 0, 0), (obj[0], obj[1], object_width, object_height))

    # Collision detection
    for obj in falling_objects:
        if (player_x < obj[0] + object_width and
            player_x + player_width > obj[0] and
            player_y < obj[1] + object_height and
            player_y + player_height > obj[1]):
            print("Game Over!")
            running = False

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
