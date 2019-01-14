#! /usr/bin/env python
import pygame
import random
class Player:
    '''定义人物初始属性'''
    def __init__(self,name,cash=50000,land=0,deposit=50000,props_card=[]):
        self.deposit = deposit                          # 存款
        self.cash = cash                                # 现金
        self.money = self.deposit + self.cash           # 总资产
        self.name = name                                # 玩家姓名
        self.land = land                                # 玩家土地数量
        # self.props_card = props_card                  # 道具卡
        self.Luck_card = 0                              # 运气卡
        self.House_Build = 0                            # 建房卡
        self.Stagnant_card = 0                          # 停滞卡



    def show(self):
        '''显示人物基础信息'''
        print('玩家姓名：', self.name)
        print('总资产：', self.money)
        print('玩家土地：', self.land,'块')
        print('现金：', self.cash)
        print('存款：', self.deposit)
        # print('道具卡: ',self.props_card)

class Building:
    '''定义土地初始文档'''
    def __init__(self,price=2000,passmoney=0,belong='',level=0,upgrade=0):
        self.belong = belong                    # 土地归属 0(无人) 1(玩家1) 2(玩家2)
        self.price = price                      # 初始土地价格
        self.level = level                      # 建筑等级
        self.passmoney = passmoney              # 过路费
        self.upgrade = upgrade                  # 土地升级费


# player1 = Player('张三')
# player1.show()
map = Building()

def buy(player,map):
    '''定义土地购买事件，玩家归属'''
    player.cash -= map.price
    player.land += 1
    player.money = player.cash + player.deposit
    map.belong = player.name
    if map.level < 3:
        map.level += 1
    else:
        map.level == 3
# buy(player1,map)
# player1.show()
# print(map.belong)
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

def LuckCard(player):
    """运气卡，百分之五十几率+现金20000，百分之五十-现金10000"""
    n = random.randint(1,10)
    if n <= 5:
        player.cash += 20000
        player.money += 20000
        print("恭喜你，中奖啦！现金+20000")
    else:
        player.cash -= 10000
        player.money -= 10000
        print("恭喜你，中奖啦！现金-10000")
    player.Luck_card -= 1

def HouseBuild(map,player):
    '''建房卡'''
    map.price = 0
    buy(player,map)
    self.House_Build -= 1

def StagnantCard(player):
    '''停滞一回合卡'''
    pass




player1 = Player('张三')
player1.show()
# HouseBuild(map,player1)
LuckCard(player1)
print('-'*20)
player1.show()


