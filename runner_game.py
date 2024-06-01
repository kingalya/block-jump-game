import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT - 70)
        self.jump = False
        self.velocity = 10     
        self.gravity = 0.5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jump:
            self.jump = True

        if self.jump:
            self.rect.y -= self.velocity
            self.velocity -= self.gravity

        if self.rect.y >= SCREEN_HEIGHT - 70:
            self.rect.y = SCREEN_HEIGHT - 70
            self.jump = False
            self.velocity = 10
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        self.rect.y = SCREEN_HEIGHT - 70

    def update(self):
        self.rect.x -= 10
        if self.rect.x < -50:
            self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100) 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Runner Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for _ in range(5):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    if pygame.sprite.spritecollideany(player, obstacles):
        running = False
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()