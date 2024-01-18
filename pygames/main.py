import pygame
import random

# Initialize the game
pygame.init()

# Creating a game (creating the background of the game window)(800 = width, 600 = height)
screen = pygame.display.set_mode((800, 600))

# Titles and Icons
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#background
background = pygame.image.load('OIP.jpg')

# Player
playerimg = pygame.image.load('spaceship1.png')
playerX = 370
playerY = 480
player_change = 0

#enemy
enemyimg = pygame.image.load('ufo.png')
enemyX = random.randint(0,737)
enemyY = random.randint(0,250)
enemyX_change = 0.3
enemyY_change = 40

def player(x, y):                     # screen blit means
    screen.blit(playerimg, (x, y))
    
def enemy(x, y):                    
    screen.blit(enemyimg, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # If keystroke is pressed, check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               player_change = 0
        if playerX <= 0:
            playerX = 0 
        elif playerX >= 736:
            playerX = 736
    enemyX += enemyX_change
    
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change
    
    # playerX += 0.1  # in this player moves right
    # playerY -= 0.1 # in this player moves up   it is related to movement of the game
    playerX += player_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

