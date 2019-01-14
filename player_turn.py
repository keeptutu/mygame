players = ['player1','player2','player3','player4']
player = 'player1'

def turn_start():
    global player
    player = 'player1'


def is_my_turn(pp):
    if pp == 'player1':
        return True

    else:
        return False


def turn_end():
    global player
    if players.index(player) <= 2:
        player = players[players.index(player) + 1]
        return player
    else:
        player = players[0]
        return player


def tou():
    pass


def jianzao():
    pass


def button_for_turnend():
    turn_end()


def buy_block():
    pass


def turn(player,block):
    tou()
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






