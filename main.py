import pygame
from pygame.locals import *
from sys import exit





title_icon = 'image/title.ico'
bg_img = 'image/bg02.jpg'
mouse = 'image/mouse.png'
block_filename = 'image/block.png'



pygame.init()
screen = pygame.display.set_mode((1600,860),0,32)
pygame.display.set_caption('大富翁')
icon = pygame.image.load(title_icon)
pygame.display.set_icon(icon)


bg = pygame.image.load(bg_img).convert()
mouse_cursor = pygame.image.load(mouse).convert_alpha()
block = pygame.image.load(block_filename).convert_alpha()


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(bg,(0,0))



    pygame.mouse.set_visible(False)
    x,y = pygame.mouse.get_pos()



    screen.blit(mouse_cursor,(x,y))

    pygame.display.update()
