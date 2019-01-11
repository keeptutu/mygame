class MAP():
    def __init__(self):
        self.ll = []
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
                y -= 64 * (41 - i)
                x = 288
                self.ll.append((x, y))
        print(self.ll)

class Player():
    def __init__(self,name='admin',money=10000,pos_x=288+7,pos_y=30+5):
        self.name = name
        self.money = money
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_up(self):
        self.pos_y += 64

    def move_down(self):
        self.pos_y -= 64

    def move_left(self):
        self.pos_x -= 64

    def move_right(self):
        self.pos_x += 64



def map_show(map,screen,block):
    for i in range(52):
        screen.blit(block,map.ll[i])



def player_move(player,pos,step):
    for i in range(step):
        if 0 <= pos + step <= 16:
            player.move_right()





