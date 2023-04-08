import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Game")

game_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)

dino = pygame.image.load("assets/Dino1.png")
dino2 = pygame.image.load("assets/Dino2.png")
dino_jump = pygame.image.load("assets/DinoJumping.png")
cactus_1 = pygame.image.load("assets/cacti/cactus1.png")
cactus_2 = pygame.image.load("assets/cacti/cactus2.png")


ground = pygame.image.load("assets/ground.png")
ground = pygame.transform.scale(ground, (1280, 20))

ground_x = 0
ground_y = 480

dino_x = 400
dino_y = 440

cactus_x = 0
cactus_y = 440
cactus = 0

counter = 0
counter2 = 0

velocity = 20
gravity = 3

speed = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("white")

# ground
    ground_x = ground_x - speed

    if ground_x == -1280:
        ground_x = 0

    screen.blit(ground, (ground_x, ground_y))
    screen.blit(ground, (ground_x + 1280, ground_y))

#cactus
    cactus_x = cactus_x - speed

    if cactus_x <= -1280:
        cactus_x = 0
        cactus = random.randrange(0, 2)

    if cactus == 1:
        screen.blit(cactus_1, (cactus_x, cactus_y))
        screen.blit(cactus_1, (cactus_x + 1280, cactus_y))

    else:
        screen.blit(cactus_2, (cactus_x, cactus_y))
        screen.blit(cactus_2, (cactus_x + 1280, cactus_y))

    if dino_x == cactus_x + 1000 and dino_y == cactus_y:
        break

# jump & dino move
    keys = pygame.key.get_pressed()
    counter = counter + 1

    if counter >= 15:
        screen.blit(dino2, (dino_x, dino_y))

        if counter >= 30:
            counter = 0
    else:
        screen.blit(dino, (dino_x, dino_y))

    if keys[pygame.K_UP]:
        velocity = 15
        velocity -= gravity
        dino_y -= velocity

        if dino_y < 380:
            dino_y = 380

    else:
        if dino_y < 440:
            velocity = 0
            velocity += gravity
            dino_y += velocity

    pygame.display.update()
    clock.tick(120)
