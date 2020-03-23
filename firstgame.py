import pygame
import random
import sys
score = 0
# change this
# initialize game
pygame.init()

# initialize screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Nice")
icon = pygame.image.load('penis.jpg')
pygame.display.set_icon(icon)

# instructions
instructionsImg = pygame.image.load('instructions.png')
instructionsImg = pygame.transform.scale(instructionsImg, (800, 600))

# picture1
picture1Img = pygame.image.load('penis.jpg')
picture1Img = pygame.transform.scale(picture1Img, (75, 75))
picture1X = 0.0
picture1Y = 0.0
picture1Xchange = 0.0
picture1Ychange = 0.0

# spot1
spot1Img = pygame.image.load('condom.png')
spot1Img = pygame.transform.scale(spot1Img, (75, 75))
# consider changing the places where the condom begins
spot1X = 400
spot1Y = 300


def picture1(x, y):
    screen.blit(picture1Img, (x, y))


def spot1(x, y):
    screen.blit(spot1Img, (x, y))


def instructions(x, y):
    screen.blit(instructionsImg, (x, y))


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                picture1Xchange = -0.5
            if event.key == pygame.K_RIGHT:
                picture1Xchange = 0.5
            if event.key == pygame.K_UP:
                picture1Ychange = -0.5
            if event.key == pygame.K_DOWN:
                picture1Ychange = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                picture1Xchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                picture1Ychange = 0

    screen.fill((255, 0, 0))
    picture1X += picture1Xchange
    picture1Y += picture1Ychange
    if picture1X < 0:
        picture1X = 0
    if picture1X > 725:
        picture1X = 725
    if picture1Y < 0:
        picture1Y = 0
    if picture1Y > 525:
        picture1Y = 525

    if (-20 < (picture1X - spot1X) < 20) and (-20 < (picture1Y - spot1Y) < 20):
        spot1X = random.randint(10, 700)
        spot1Y = random.randint(10, 500)
        score += 1
        if score == 10:
            sys.exit()
    instructions(0, 0)
    picture1(picture1X, picture1Y)
    spot1(spot1X, spot1Y)

    pygame.display.update()
