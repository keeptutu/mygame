import random
'''
地图块类及生成显示
玩家类及玩家移动
'''


#  创建地图类
class MAP:
    def __init__(self):
        self.ll = []  # 地图块需要显示的坐标
        for i in range(52):
            x = 288
            y = 30
            if i < 16:
                x += 64 * i
                self.ll.append((x,y))


            elif i < 26:
                x = 15 * 64 + 288
                y -= 64 * (15 - i)

                self.ll.append((x, y))
            elif i < 42:
                y = 30 + 64 * 11
                x += 64 * (41 - i)
                self.ll.append((x, y))
            else:
                y += 64 * (41 - i) + 704
                x = 288
                self.ll.append((x, y))
        print(self.ll)  # 测试用输出





class Player():
    def __init__(self,name='admin',money=10000,pos=0, pos_x=288+7,pos_y=30+5):
        self.name = name
        self.money = money
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = pos

    def move_up(self):
        self.pos_y += 64
        self.pos += 1

    def move_down(self):
        self.pos_y -= 64
        self.pos += 1

    def move_left(self):
        self.pos_x -= 64
        self.pos += 1

    def move_right(self):
        self.pos_x += 64
        self.pos += 1

    def player_move(self):

        if 0 <= self.pos < 15:
            self.move_right()
        elif 15 <= self.pos < 26:
            self.move_up()
        elif 26 <= self.pos < 41:
            self.move_left()
        elif 41 <= self.pos < 52:
            self.move_down()
        elif self.pos == 52:
            self.pos -= 52
            self.move_right()

    def step(self):
        st = random.randint(1,6)
        for i in range(st):
            self.player_move()


def map_show(maps,screen,block):
    for i in range(52):
        screen.blit(block,maps.ll[i])










