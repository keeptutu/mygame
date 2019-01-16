from aboutrect import *
from gamestart import *
from player_turn import *
from gamadata import *
from mysprite import *
import pygame
from pygame.locals import *
from sys import exit
import random
from filename import *
import time

#  更多的文件都通过filename文件进行了导入
kuang_filename = 'image/kuang2.png'  # block的红色框框的图片路径
yes_filename = 'image/yes.png'  # yes按钮的图片文件路径
no_filename = 'image/no.png'  # no按钮的图片文件路径
player_filename = 'image/pp.png'  # 测试用玩家图片文件路径
yes = 'image/yes.png' # yes按钮的文件路径
no = 'image/no.png'  # no按钮的文件路径
# pygame模块初始化
game_start()  # 由gamestart.py导入
pygame.init()  # pygame模块的初始化 让硬件做好准备

screen = pygame.display.set_mode((1600,860),0,32) # 创建游戏主屏幕

pygame.display.set_caption('大富翁')  # 给游戏窗口创建名称

icon = pygame.image.load(title_icon)  # 加载游戏窗口的图片
pygame.display.set_icon(icon)  # 设置窗口图标

# 游戏图片预载
bg = pygame.image.load(bg_img).convert()
mouse_cursor = pygame.image.load(mouse).convert_alpha()
block = pygame.image.load(block_filename).convert_alpha()
block_h = pygame.image.load(block_filename2).convert_alpha()
# yes_button = pygame.image.load(yes_filename).convert_alpha()
# no_button = pygame.image.load(no_filename).convert_alpha()
pp = pygame.image.load(player_filename).convert_alpha()
kuang = pygame.image.load(kuang_filename).convert_alpha()
myrect1 = pygame.Rect((0,0),(240,360))  # 此为测试rect
# myrect1.move_ip(-50,-100)


# 游戏文字字体 设置字体和大小
my_font = pygame.font.Font('rex2.ttf',32)

# 文字内容和文字的颜色
text = my_font.render('你好', True, (255, 255, 255))

framerate = pygame.time.Clock()
dice = Mysprite(screen)
dice.load('image/两排64.png', 64, 64, 3)

group = pygame.sprite.Group()

group.add(dice)
a = MAP()  # 实例化地图块 Map类由gamedata文件导入
pl = Player()  # 实力化玩家 Player类由gamedata文件导入


for i in createrect(a.ll):  # 由aboutrect文件导入 用于给每一个block地图块创建对应的rect对象 a.ll是Map对象中的位置列表
    print(i)  # 测试用输出
    exec(i)  # 循环执行
block_list = [] # 创建一个空列表
for i in range(len(a.ll)):  # 通过for循环把每个block的rect对象放在一个列表里面
    exec('block_list.append(testrect'+str(i)+')')
    print(block_list)


def show_text(word,screen,pos):  # 创建一个函数用于在屏幕上显示文字
    text = my_font.render(word,True,(255,255,255))
    screen.blit(text,pos)


def show_button(pic,screen,pos): # 创建一个函数用于在屏幕上显示按钮
    pics = pygame.image.load(pic).convert_alpha()
    screen.blit(pics,pos)
    rect = pygame.Rect(pos,(pics.get_size()))
    return rect  # 这个函数在进行了按钮图像的显示后返回了一个按钮的rect对象 方便其他使用


# 此处可以设置循环外部条件  用作循环内的条件控制
tou = True  # 骰子精灵显示
player_info = True  # 玩家信息板块
# 创建游戏循环
while 1:
    x, y = pygame.mouse.get_pos()  # 通过pygame模块捕获鼠标的坐标值x,y 方便判断鼠标你的位置
    framerate.tick(100)
    ticks = pygame.time.get_ticks()
    # print(ticks)
    screen.blit(bg, (0, 0))  # 显示背景
    if player_info is True:  # 通过外部的player_info变量判断是否显示人物信息框
        pygame.draw.rect(screen,(255,0,0),myrect1)  # 在屏幕上绘制rect

    group.update(ticks,100)
    if tou is True:  # 通过外部的tou变量判断是否显示骰子的动画
        group.draw(screen)
    yes_button = show_button(yes,screen,(600,600))  # 通过show_button函数在屏幕上显示yes按钮并把按钮的rect对象赋给yes_button
    no_button = show_button(no,screen,(860,600))  # 通过show_button函数在屏幕上显示yes按钮并把按钮的rect对象赋给y_button
    # pygame模块中的事件捕捉
    for event in pygame.event.get():
        if event.type == QUIT:  # 如果产生点击窗口关闭的事件
            exit()  # 退出
        if event.type == KEYDOWN:  # 如果产生键盘按键的事件
            if event.key == pygame.K_ESCAPE:  # 如果按下的键是esc
                exit()  # 退出
        if event.type == MOUSEBUTTONDOWN:  # 如果产生了鼠标事件
            if yes_button.collidepoint(x,y):  # 如果鼠标(坐标) 在yes按钮的rect对象矩形内
                pressed_array = pygame.mouse.get_pressed()  # 建立鼠标按键事件的数组列表
                for index in range(len(pressed_array)):  # 遍历列表中的每一个元素
                    if pressed_array[index]:
                        if index == 0:  # 如果index == 0 即代表此次的鼠标事件为鼠标的左键点击
                            pl.step()  # 条件执行 pl为Player类的实例对象 执行step函数进行人物图像的移动

    map_show(a,screen,block)  # 该函数由gamedata导入 用于显示block块
    screen.blit(pp,(pl.pos_x,pl.pos_y))  # 在屏幕上绘制玩家人物

    # screen.blit(t1, (800, 600))
    pygame.mouse.set_visible(False)  # 隐藏原始鼠标图标

    # if myrect1.collidepoint(x,y):
    for i in block_list:  # block_list列表中的元素对应每个地图快的topleft数值,保存为元组
        if i.collidepoint(x,y):  # 遍历列表判定鼠标在哪一个block上

            screen.blit(kuang,i.topleft) # 显示框

    screen.blit(text,(500,500))  # 文字显示
    # show_text('wo',screen,(600,600))

    screen.blit(mouse_cursor, (x, y))  # 在鼠标(坐标)位置显示鼠标的图像

    pygame.display.update()  # 刷新屏幕  根据绘制的顺序显示图片 所以在屏幕中进行绘制时要按照自己的需求来安排绘制语句的先后

