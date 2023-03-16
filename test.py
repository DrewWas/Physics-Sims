import pygame
import math

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TIME_STEP = 0.05  # simulation time step in seconds
SCALE = 0.1  # pixel to meter scale factor

class Projectile:
    def __init__(self, velocity, angle, height):
        self.velocity = velocity
        self.angle = math.radians(angle)
        self.height = height
        self.x = 0
        self.y = height

        self.vx = velocity * math.cos(self.angle)
        self.vy = velocity * math.sin(self.angle)

        self.g = 9.81

    def update(self):
        self.x += self.vx * TIME_STEP
        self.y += self.vy * TIME_STEP
        self.vy += self.g * TIME_STEP

    def draw(self, screen):
        x = int(self.x * SCALE)
        y = SCREEN_HEIGHT - int(self.y * SCALE)
        pygame.draw.circle(screen, BLUE, (x, y), 5)

    def is_out_of_screen(self):
        return self.x * SCALE > SCREEN_WIDTH or self.y * SCALE < 0

class ProjectileMotionSimulator:
    def __init__(self):
        self.projectiles = []

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Projectile Motion Simulator")

    def run(self):
        clock = pygame.time.Clock()

        # Main game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.add_projectile()

            # Update projectiles
            for projectile in self.projectiles:
                projectile.update()

            # Remove projectiles that are out of screen
            self.projectiles = [projectile for projectile in self.projectiles if not projectile.is_out_of_screen()]

            # Clear screen
            self.screen.fill(WHITE)

            # Draw projectiles
            for projectile in self.projectiles:
                projectile.draw(self.screen)

            # Update display
            pygame.display.flip()

            # Limit frame rate
            clock.tick(1 / TIME_STEP)

        # Clean up Pygame
        pygame.quit()

    def add_projectile(self):
        try:
            velocity = float(input("Initial Velocity (m/s): "))
            angle = float(input("Launch Angle (degrees): "))
            height = float(input("Initial Height (m): "))
        except ValueError:
            print("Invalid input")
            return

        projectile = Projectile(velocity, angle, height)
        self.projectiles.append(projectile)

simulator = ProjectileMotionSimulator()
simulator.run()
