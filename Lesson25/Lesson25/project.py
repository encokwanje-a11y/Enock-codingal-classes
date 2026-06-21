import pygame
import random
import sys
import math

# Initialize
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 60, 60)
GREEN = (50, 255, 100)
BLUE = (80, 120, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (180, 60, 255)
CYAN = (0, 255, 255)

class Player:
    def __init__(self):
        self.width = 40
        self.height = 30
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 80
        self.speed = 6
        self.health = 100
        self.max_health = 100
        
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed
    
    def draw(self, screen):
        # Ship body
        points = [
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ]
        pygame.draw.polygon(screen, CYAN, points)
        pygame.draw.polygon(screen, WHITE, points, 2)
        
        # Health bar
        bar_width = 50
        bar_height = 6
        bar_x = self.x + self.width // 2 - bar_width // 2
        bar_y = self.y - 15
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, RED, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width * health_ratio, bar_height))

class Asteroid:
    def __init__(self, level):
        self.size = random.randint(20, 50)
        self.x = random.randint(0, WIDTH - self.size)
        self.y = -self.size
        self.speed = random.uniform(2, 4 + level * 0.5)
        self.rotation = 0
        self.rotation_speed = random.uniform(-3, 3)
        self.points = []
        # Generate rocky shape
        for i in range(8):
            angle = i * math.pi / 4
            radius = self.size // 2 + random.randint(-5, 5)
            px = math.cos(angle) * radius
            py = math.sin(angle) * radius
            self.points.append((px, py))
    
    def update(self):
        self.y += self.speed
        self.rotation += self.rotation_speed
    
    def draw(self, screen):
        rotated_points = []
        for px, py in self.points:
            rx = px * math.cos(math.radians(self.rotation)) - py * math.sin(math.radians(self.rotation))
            ry = px * math.sin(math.radians(self.rotation)) + py * math.cos(math.radians(self.rotation))
            rotated_points.append((self.x + self.size // 2 + rx, self.y + self.size // 2 + ry))
        pygame.draw.polygon(screen, (120, 100, 80), rotated_points)
        pygame.draw.polygon(screen, WHITE, rotated_points, 2)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

class PowerUp:
    def __init__(self):
        self.size = 25
        self.x = random.randint(0, WIDTH - self.size)
        self.y = -self.size
        self.speed = 3
        self.type = random.choice(['health', 'shield'])
        self.pulse = 0
    
    def update(self):
        self.y += self.speed
        self.pulse += 0.1
    
    def draw(self, screen):
        glow = int(127 + 127 * math.sin(self.pulse))
        color = GREEN if self.type == 'health' else PURPLE
        pygame.draw.circle(screen, color, (int(self.x + self.size // 2), int(self.y + self.size // 2)), self.size // 2)
        pygame.draw.circle(screen, (glow, glow, glow), (int(self.x + self.size // 2), int(self.y + self.size // 2)), self.size // 2, 3)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)
        self.life = 30
        self.color = color
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
    
    def draw(self, screen):
        if self.life > 0:
            alpha = int(255 * (self.life / 30))
            size = int(4 * (self.life / 30))
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), size)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Dodge")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.reset()
    
    def reset(self):
        self.player = Player()
        self.asteroids = []
        self.powerups = []
        self.particles = []
        self.score = 0
        self.level = 1
        self.asteroid_timer = 0
        self.powerup_timer = 0
        self.game_over = False
        self.shield_time = 0
    
    def spawn_asteroid(self):
        self.asteroids.append(Asteroid(self.level))
    
    def spawn_powerup(self):
        if random.random() < 0.3:
            self.powerups.append(PowerUp())
    
    def create_explosion(self, x, y, color):
        for _ in range(20):
            self.particles.append(Particle(x, y, color))
    
    def check_collisions(self):
        player_rect = pygame.Rect(self.player.x, self.player.y, self.player.width, self.player.height)
        
        # Asteroid collisions
        for asteroid in self.asteroids[:]:
            if player_rect.colliderect(asteroid.get_rect()):
                if self.shield_time <= 0:
                    self.player.health -= 20
                    self.create_explosion(asteroid.x + asteroid.size // 2, asteroid.y + asteroid.size // 2, RED)
                self.asteroids.remove(asteroid)
                if self.player.health <= 0:
                    self.game_over = True
        
        # PowerUp collisions
        for powerup in self.powerups[:]:
            if player_rect.colliderect(powerup.get_rect()):
                if powerup.type == 'health':
                    self.player.health = min(self.player.max_health, self.player.health + 30)
                else:
                    self.shield_time = 300  # 5 seconds at 60 FPS
                self.create_explosion(powerup.x + powerup.size // 2, powerup.y + powerup.size // 2, YELLOW)
                self.powerups.remove(powerup)
    
    def update(self):
        if self.game_over:
            return
        
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        
        # Spawn asteroids
        self.asteroid_timer += 1
        spawn_rate = max(10, 40 - self.level * 3)
        if self.asteroid_timer >= spawn_rate:
            self.spawn_asteroid()
            self.asteroid_timer = 0
        
        # Spawn powerups
        self.powerup_timer += 1
        if self.powerup_timer >= 180:  # Every 3 seconds
            self.spawn_powerup()
            self.powerup_timer = 0
        
        # Update asteroids
        for asteroid in self.asteroids[:]:
            asteroid.update()
            if asteroid.y > HEIGHT:
                self.asteroids.remove(asteroid)
                self.score += 10
        
        # Update powerups
        for powerup in self.powerups[:]:
            powerup.update()
            if powerup.y > HEIGHT:
                self.powerups.remove(powerup)
        
        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if particle.life <= 0:
                self.particles.remove(particle)
        
        # Update shield
        if self.shield_time > 0:
            self.shield_time -= 1
        
        # Level up
        if self.score > 0 and self.score % 500 == 0:
            self.level = self.score // 500 + 1
        
        self.check_collisions()
    
    def draw_stars(self):
        for i in range(50):
            x = (i * 37) % WIDTH
            y = (i * 73 + pygame.time.get_ticks() // 50) % HEIGHT
            pygame.draw.circle(self.screen, WHITE, (x, y), 1)
    
    def draw(self):
        self.screen.fill(BLACK)
        self.draw_stars()
        
        if not self.game_over:
            # Draw shield
            if self.shield_time > 0:
                pygame.draw.circle(self.screen, PURPLE, 
                                 (int(self.player.x + self.player.width // 2), 
                                  int(self.player.y + self.player.height // 2)), 
                                 35, 3)
            
            self.player.draw(self.screen)
            
            for asteroid in self.asteroids:
                asteroid.draw(self.screen)
            
            for powerup in self.powerups:
                powerup.draw(self.screen)
            
            for particle in self.particles:
                particle.draw(self.screen)
            
            # UI
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            level_text = self.font.render(f"Level: {self.level}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(level_text, (10, 50))
            
            if self.shield_time > 0:
                shield_text = self.small_font.render(f"Shield: {self.shield_time // 60 + 1}s", True, PURPLE)
                self.screen.blit(shield_text, (10, 90))
        
        else:
            # Game over screen
            game_over_text = self.font.render("GAME OVER", True, RED)
            score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
            level_text = self.font.render(f"Level Reached: {self.level}", True, WHITE)
            restart_text = self.small_font.render("Press R to restart or ESC to quit", True, WHITE)
            
            self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 80))
            self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 20))
            self.screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 2 + 20))
            self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 70))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_r and self.game_over:
                        self.reset()
            
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()