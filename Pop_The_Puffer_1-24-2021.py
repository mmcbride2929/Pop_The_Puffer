import pygame
import random
import math

pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# display caption and icon
pygame.display.set_caption("Pop The Puffer!")
icon = pygame.image.load('pufferfish.png')
pygame.display.set_icon(icon)

# puffer fish sprite
puffer_img = pygame.image.load('puffer-fish.png')
pufferX = 374
pufferY = 260

# puffer fish movement
pufferX_movement = 0
pufferY_movement = 0

# horizontal needle sprite
Hneedle_img = []
HneedleX = []
HneedleY = []
Hneedle_movement = []
enemy_num = 3

for i in range(enemy_num):
    Hneedle_img.append(pygame.image.load('seaurchin.png'))
    HneedleX.append(-80)
    HneedleY.append(random.randint(60, 525))
    Hneedle_movement.append(.35)


def puffer(x, y):
    screen.blit(puffer_img, (pufferX, pufferY))


def Hneedle(x, y, i):
    screen.blit(Hneedle_img[i], (HneedleX[i], HneedleY[i]))


def collision(pufferX, pufferY, HneedleX, HneedleY):
    distance = math.sqrt((math.pow(pufferX - HneedleX, 2)) + (math.pow(pufferY - HneedleY, 2)))
    if distance < 37:
        print(distance)
        return True
    else:
        return False


# display loop
running = True
while running:

    # blue background
    screen.fill((0, 0, 222))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed checked whether it's up down left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pufferY_movement = -.2
            if event.key == pygame.K_DOWN:
                pufferY_movement = .2
            if event.key == pygame.K_LEFT:
                pufferX_movement = -.2
            if event.key == pygame.K_RIGHT:
                pufferX_movement = .2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pufferX_movement = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pufferY_movement = 0

    # puffer boundaries
    pufferY += pufferY_movement
    pufferX += pufferX_movement
    if pufferX <= 0:
        pufferX = 0
    if pufferX >= 736:
        pufferX = 736
    if pufferY <= 0:
        pufferY = 0
    if pufferY >= 539:
        pufferY = 539

    for i in range(enemy_num):
        # Urchin Horizontal Spawn
        HneedleX[i] += Hneedle_movement[i]
        if HneedleX[i] >= 800:
            HneedleX[i] = 0
            HneedleY[i] = random.randint(60, 525)

        iscollision = collision(pufferX, pufferY, HneedleX[i], HneedleY[i])
        if iscollision:
            break

        Hneedle(HneedleX[i], HneedleY[i], i)

    puffer(pufferX, pufferY)

    pygame.display.update()
