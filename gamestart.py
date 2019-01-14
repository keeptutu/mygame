import pygame
from pygame.locals import *
from sys import *

def game_start():
    pygame.init()
    screen = pygame.display.set_mode((800,600),0,32)

    n = 1
    while n:
        for event in pygame.event.get():
            if event.type == QUIT:
                n = 0
        pygame.display.update()


if __name__ == '__main__':
    game_start()