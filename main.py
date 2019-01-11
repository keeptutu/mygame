from gamadata import *
from mysprite import *
import pygame
from pygame.locals import *
from sys import exit
import random
from filename import *
import time


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

myrect1 = pygame.Rect(0,0,240,360)

# 游戏文字字体 设置字体和大小
my_font = pygame.font.Font('rex2.ttf',32)

# 文字内容和文字的颜色
text = my_font.render('你好', True, (255, 255, 255))

framerate = pygame.time.Clock()
dice = Mysprite(screen)
dice.load('image/两排64.png', 64, 64, 3)

group = pygame.sprite.Group()

group.add(dice)
a = MAP()  # 实例化地图块
pl = Player()  # 实力化玩家
tou = True  # 骰子精灵显示
player_info = False  # 玩家信息板块
# 创建游戏循环
while 1:
    framerate.tick(100)
    ticks = pygame.time.get_ticks()
    # print(ticks)
    screen.blit(bg, (0, 0))  # 显示背景
    if player_info is True:
        pygame.draw.rect(screen,(255,0,0),myrect1)

    group.update(ticks,100)
    if tou is True:
        group.draw(screen)
    # pygame模块中的事件捕捉
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pl.step()
                print(pl.pos)

    map_show(a,screen,block)
    screen.blit(pp,(pl.pos_x,pl.pos_y))

    # screen.blit(t1, (800, 600))
    pygame.mouse.set_visible(False)
    x,y = pygame.mouse.get_pos()

    screen.blit(text,(800,430))  # 文字显示
    screen.blit(yes_button,(500,600))  # 按钮显示
    screen.blit(no_button,(900,600))
    screen.blit(mouse_cursor, (x, y))  # 鼠标的图像显示

    # 屏幕刷新
    pygame.display.update()

