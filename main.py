import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("この世は、終わりだインベーダー")
player = pygame.image.load("player.png")
playerX = 200
playerY = 200

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(player, (playerX, playerY))
    # 押されたキーをしらべる

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_LEFT]:
        playerX -= 0.7

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_RIGHT]:
        playerX += 0.7

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_UP]:
        playerY -= 0.7

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_DOWN]:
        playerY += 0.7

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == KEYDOWN:
        #     if event.key == K_RIGHT:
        #         playerX += 7
        #         screen.fill((255,0,0))
        #     if event.key == K_LEFT:
        #         playerX -= 10
        #         screen.fill((0,255,0))
        #     if event.key == K_UP:
        #         playerY -= 10
        #         screen.fill((0,0,255))
        #     if event.key == K_DOWN:
        #         playerY += 10
        #         screen.fill((0,0,0))



    pygame.display.update()



