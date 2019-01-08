import pygame, sys,time

screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('动画测试')
image = pygame.image.load('image/一排64.png')
rect = image.get_rect()
rect2 = pygame.Rect(0, 0, rect.width // 6, rect.height)
tick = pygame.time.Clock()


while 1:
    clock = pygame.time.Clock()
    # 初始化Clock对象
    # time_passed = clock.tick()
    # 返回上一个调用的时间（ms）
    time_passed = clock.tick(1)
    # 在么一个循环中加上它，其中的参数就成为了游戏的最大帧率，避免游戏占用所有的CPU资源。

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for n in range(6):
        tick.tick(10)
        rect2.x += n * rect2.width
        if rect2.x > 384:
            rect2.x = 0
        screen.fill((255, 255, 255))
        screen.blit(image,(0, 0),rect2)  # 这里给了3个实参，分别是图像，绘制的位置，绘制的截面框
        pygame.display.flip()



