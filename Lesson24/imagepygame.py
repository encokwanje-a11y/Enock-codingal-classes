import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Create display
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dancing Penguin")

# Load images safely
try:
    background_image = pygame.transform.scale(
        pygame.image.load("background.png").convert(),
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    penguin_image = pygame.transform.scale(
        pygame.image.load("penguin.png").convert_alpha(),
        (200, 200)
    )

except FileNotFoundError:
    print("Image file not found!")
    pygame.quit()
    sys.exit()

# Penguin position and movement
penguin_rect = penguin_image.get_rect(center=(250, 250))
speed_x = 3
speed_y = 2

# Font
font = pygame.font.Font(None, 40)

# Colors for changing text
colors = [
    pygame.Color("red"),
    pygame.Color("blue"),
    pygame.Color("green"),
    pygame.Color("purple"),
    pygame.Color("orange")
]
color_index = 0

# Clock
clock = pygame.time.Clock()

running = True

while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move penguin
    penguin_rect.x += speed_x
    penguin_rect.y += speed_y

    # Bounce off walls
    if penguin_rect.left <= 0 or penguin_rect.right >= SCREEN_WIDTH:
        speed_x *= -1

    if penguin_rect.top <= 0 or penguin_rect.bottom >= SCREEN_HEIGHT:
        speed_y *= -1

    # Change text color
    color_index = (color_index + 1) % len(colors)

    text = font.render(
        "Hello World! Welcome!",
        True,
        colors[color_index]
    )

    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 460))

    # Draw everything
    display_surface.blit(background_image, (0, 0))
    display_surface.blit(penguin_image, penguin_rect)
    display_surface.blit(text, text_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()