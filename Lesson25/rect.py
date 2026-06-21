import pygame

# Initialize Pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 640, 480

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set caption
pygame.display.set_caption("My First Game Screen")

# Colors
BLACK = (0, 0, 0)      # Background color
BLUE = (0, 0, 255)     # Rectangle color
WHITE = (255, 255, 255)  # Text color

# Font for text
font = pygame.font.Font(None, 36)

# Create text
text = font.render("Welcome to My First Game Screen!", True, WHITE)

# Rectangle dimensions
rect_width = 120
rect_height = 80

# Center rectangle
rect_x = (WIDTH - rect_width) // 2
rect_y = (HEIGHT - rect_height) // 2

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BLACK)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Display text
    screen.blit(text, (120, 50))

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()