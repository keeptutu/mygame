#! /usr/bin/env python
import Attribute
def buy(player,map):
    '''定义土地购买事件'''
    player.cash -= map.price
    player.land += 1
    player.money = player.cash + player.deposit
    map.belong = player.name
buy(player1,map)
player1.show()
print(map.belong)

def house_level(map):
    '''根据土地等级，划分过路费'''
    if map.level == 0:              # 0级
        map.price = 0
    elif map.level == 1:            # 1级
        map.price = 3000
    elif map.level == 2:            # 2级
        map.price = 7500
    else:                           # 3级
        map.price = 12000

def house_upgrade(map):
    '''土地升级费,土地等级变更,过路费变更'''
    if map.level == 0:
        map.upgrade = 2500
        map.passmoney = 3000
    elif map.level == 1:
        map.upgrade = 5000
        map.passmoney = 7500
    elif map.level == 2:
        map.upgrade = 7500
        map.passmoney = 12000


def Pass_money(player,map,other):
    '''支付过路费'''
    player.cash -= map.passmoney
    player.money = player.deposit + player.cash
    other.cash += map.passmoney
    other.money = other.deposit + other.cash




