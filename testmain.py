import pygame
from pygame import *
from sys import exit


bg_img = 'image/bg02.jpg'

pygame.init()
screen = pygame.display.set_mode((1600,800),0,32)
bg = pygame.image.load(bg_img).convert()




while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()



    screen.blit(bg, (0, 0))
    pygame.display.update()