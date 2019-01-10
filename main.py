from mysprite import *
import pygame
from pygame.locals import *
from sys import exit
import random
from filename import *
import time
import threading




# 图片路径
# title_icon = 'image/title.ico'
# bg_img = 'image/bg02.jpg'
# mouse = 'image/mouse.png'
# block_filename = 'image/block.png'
# block_filename2 = 'image/block_blue.png'
touzi_1 = 'image/t1.png'
touzi_2 = 'image/t2.png'
touzi_3 = 'image/t3.png'
touzi_4 = 'image/t4.png'
touzi_5 = 'image/t5.png'
touzi_6 = 'image/t6.png'

yes_filename = 'image/yes.png'
no_filename = 'image/no.png'
player_filename = 'image/pp.png'
# pygame模块初始化
pygame.init()
# 屏幕创建
screen = pygame.display.set_mode((1600,860),0,32)
# 添加标题
pygame.display.set_caption('大富翁')
# 改变游戏的图标
icon = pygame.image.load(title_icon)
pygame.display.set_icon(icon)

# 游戏图片预载
bg = pygame.image.load(bg_img).convert()
mouse_cursor = pygame.image.load(mouse).convert_alpha()
block = pygame.image.load(block_filename).convert_alpha()
block_h = pygame.image.load(block_filename2).convert_alpha()
yes_button = pygame.image.load(yes_filename).convert_alpha()
no_button = pygame.image.load(no_filename).convert_alpha()
pp = pygame.image.load(player_filename).convert_alpha()






# 游戏文字字体
my_font = pygame.font.Font('rex2.ttf',32)

text = my_font.render('你好',True,(255,255,255))


framerate = pygame.time.Clock()
dice = Mysprite(screen)
dice.load('image/两排64.png',64,64,3)

group = pygame.sprite.Group()

group.add(dice)


# 创建游戏循环
while 1:
    framerate.tick(60)
    ticks = pygame.time.get_ticks()
    print(ticks)
    screen.blit(bg, (0, 0))
    group.update(ticks,150)
    group.draw(screen)
    # pygame模块中的事件捕捉
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
    # 在屏幕上显示背景图片


    # 通过循环 创建地图块
    for i in range(52):
        x = 288
        y = 30
        if i < 16:
            x += 64*i

            screen.blit(block,(x,y))
        elif i < 26:
            x = 15*64 + 288
            y -= 64*(15-i)

            screen.blit(block,(x,y))
        elif i < 42:
            y = 30 + 64*11
            x += 64*(41-i)
            screen.blit(block,(x,y))
        else:
            y -= 64*(41-i)
            x = 288
            screen.blit(block,(x,y))

    screen.blit(block_h,(288,30))

    screen.blit(pp,(288+7,30+5))

    # screen.blit(t1, (800, 600))
    pygame.mouse.set_visible(False)
    x,y = pygame.mouse.get_pos()

    screen.blit(text,(800,430))
    screen.blit(yes_button,(500,600))
    screen.blit(no_button,(900,600))
    screen.blit(mouse_cursor, (x, y))

    # 屏幕刷新
    pygame.display.update()

