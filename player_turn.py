players = ['player1','player2','player3','player4']  # 建立玩家列表 游戏默认有四个玩家
player = 'player1'  # 用player变量来确定当前玩家是谁,可作为循环内的判断条件


def turn_start():  # 定义函数 表示游戏开始 当前玩家是player1
    global player  # 此时应该通过global来使用外部的player
    player = 'player1'


# def is_my_turn(nowplayer):  # 定义函数用来判断当前玩家是哪一个玩家 用于联网多人
#     if nowplayer == player:
#         return True
#
#     else:
#         return False


def turn_end():  # 定义回合结束函数
    global player  # 使用外部的player变量
    if players.index(player) <= 2:  # 通过条件判断 切换到下一个玩家
        player = players[players.index(player) + 1]
        return player
    else:
        player = players[0]
        return player


def tou():  # 定义掷骰子的函数
    pass


def move(): # 代表人物移动
    pass


def jianzao():  # 定义block上房屋建造的函数
    pass


def button_for_turnend():  # 回合结束按钮的点击
    turn_end()


def buy_block():  # 购买block的对话按钮 按下yes返回True 按下no返回False
    pass


def turn(player,block):  # 游戏的回合内逻辑
    tou()  # 掷骰子
    move()  # 人物移动

    if block.belong == player.belong:
        if block.buildlevel < 3:
            if player.money >= block.update_money:
                if jianzao():
                    player.money -= block.update_money
                    block.buildlevel += 1

                else:
                    button_for_turnend()
            else:
                button_for_turnend()
        else:
            button_for_turnend()
    elif block.belong == 0:
        if player.money >= block.buymoney:
            if buy_block():
                player.money -= block.buymoney
                block.belong = player.belong
                block.buildlevel = 0
                button_for_turnend()
            else:
                button_for_turnend()
        else:
            button_for_turnend()

    else:
        if player.money >= block.passmoney:
            player.money -= block.passmoney
            eval('player'+str(block.belong)+'.money+=block.passmoney')
            button_for_turnend()
        elif player.money + player.diyamoney >= block.passmoney:
            player.mortgage()
            player.money -= block.passmoney
            eval('player' + str(block.belong) + '.money+=block.passmoney')
        else:
            player.lose()


if __name__ == '__main__':
    turn_start()
    print(turn_end())
    print(turn_end())
    print(turn_end())
    print(turn_end())
    print(turn_end())
    print(turn_end())






