import pygame
from pygame.locals import *
from sys import exit
import random


# touzi1 = 'image/t1.png'
# touzi2 = 'image/t2.png'
# touzi3 = 'image/t3.png'
# touzi4 = 'image/t4.png'
# touzi5 = 'image/t5.png'
# touzi6 = 'image/t6.png'

def tou():
    i = random.randint(1,6)
    print(i)
    touzi = pygame.image.load('image/t' + str(i) + '.png')
    return touzi
tou()
