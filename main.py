import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("この世は、終わりだインベーダー")
img = pygame.image.load("player.png")
x = 200
y = 200

running = True
while running:
    screen.blit(img, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                screen.fill((255,0,0))
            if event.key == K_LEFT:
                screen.fill((0,255,0))
            if event.key == K_UP:
                screen.fill((0,0,255))
            if event.key == K_DOWN:
                screen.fill((0,0,0))



    pygame.display.update()




