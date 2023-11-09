'''
10/9/2023
Group 8:
1.Gwendolyn Stephenson
2.Jamal Brown
3.Derrick Chesire
'''
import pygame
import random
import sys
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# Initializing the library pygame
pygame.init()

# Initializing the constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 1
ENEMY_COUNT = 6

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Creating the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
start = 6000



# loading images into the game as characters
player_img = pygame.image.load("player.PNG")
player_rect = player_img.get_rect()
bullet_img = pygame.image.load("bullet.PNG")
enemy_img = pygame.image.load("enemy.PNG")

# Initialize player position
player_rect.centerx = WIDTH/2
player_rect.bottom = HEIGHT - 10

# Initialize enemy positions
enemies = []
for _ in range(ENEMY_COUNT):
    enemy = enemy_img.get_rect()
    enemy.x = random.randint(0, WIDTH - enemy.width)
    enemy.y = random.randint(50, 300)
    enemies.append(enemy)

# Initialize bullets list
bullets = []

# create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED

    # Shooting
    if keys[pygame.K_SPACE]:
        bullet_rect = bullet_img.get_rect()
        bullet_rect.centerx = player_rect.centerx
        bullet_rect.top = player_rect.top     
        bullets.append(bullet_rect)

    # move bullets
    bullets = [bullet for bullet in bullets if bullet.y > 0]
    for bullet in bullets:
        bullet.y -= BULLET_SPEED

    # move enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > HEIGHT:
            enemy.x = random.randint(0, WIDTH - enemy.width)
            enemy.y = random.randint(-300, -enemy.height)

    # collision detection
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            pygame.quit()
            sys.exit()
        for bullet in bullets:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemy.x = random.randint(0, WIDTH - enemy.width)
                enemy.y = random.randint(-300, -enemy.height)

    # Draw everything
    screen.fill(BLACK)
    screen.blit(player_img, player_rect)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    # update the display
    pygame.display.flip()

    # control the frame rate
    clock.tick(60)

    #timer
    start -= 1
    if start <= 0:
        pygame.quit()
        sys.exit()







