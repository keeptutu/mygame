#! /usr/bin/env python
import pygame
import random


class Player:
    '''定义人物初始属性'''
    def __init__(self,name,belong,money=50000):
        self.belong = belong
        self.money = money                                # 现金
        self.name = name                                # 玩家姓名
        self.land = []                                # 玩家土地数量





class Block:
    '''定义土地初始文档'''
    def __init__(self,buymoney=2000,passmoney=0,belong=0,buildlevel=0,update_money=0,mortgage=0):
        self.belong = belong                    # 土地归属 0(无人) 1(玩家1) 2(玩家2)
        self.buymoney = buymoney                # 初始土地价格
        self.buildlevel = buildlevel            # 建筑等级
        self.passmoney = passmoney              # 过路费
        self.update_money = update_money        # 土地升级费
        self.mortgage = mortgage

def buy_block(player,block):
    player.momey -= block.buymoney
    block.belong = player.belong
    block.mortgage += 0.5 * block.buymoney


def block_build(player,block):
    player.money -= block.update_money
    block.buildlevel += 1
    block.mortgage += 0.5 * block.update_money

def pay_passmoney(payplayer,getplayer,block):
    payplayer.money -= block.passmoney
    getplayer.money += block.passmoney






# def mortgage(player,block):











# player1 = Player('张三')
# player1.show()

# def buy(player,map):
#     '''定义土地购买事件，玩家归属'''
#     player.cash -= map.price
#     player.land += 1
#     player.money = player.cash + player.deposit
#     map.belong = player.name
#     if map.level < 3:
#         map.level += 1
#     else:
#         map.level == 3
# # buy(player1,map)
# # player1.show()
# # print(map.belong)
# def house_level(map):
#     '''根据土地等级，划分过路费'''
#     if map.level == 0:              # 0级
#         map.price = 0
#     elif map.level == 1:            # 1级
#         map.price = 3000
#     elif map.level == 2:            # 2级
#         map.price = 7500
#     else:                           # 3级
#         map.price = 12000

#def house_upgrade(map):
#     '''土地升级费,土地等级变更,过路费变更'''
#     if map.level == 0:
#         map.upgrade = 2500
#         map.passmoney = 3000
#     elif map.level == 1:
#         map.upgrade = 5000
#         map.passmoney = 7500
#     elif map.level == 2:
#         map.upgrade = 7500
#         map.passmoney = 12000
#
#
# def Pass_money(player,map,other):
#     '''支付过路费'''
#     player.cash -= map.passmoney
#     player.money = player.deposit + player.cash
#     other.cash += map.passmoney
#     other.money = other.deposit + other.cash
#
# def LuckCard(player):
#     """运气卡，百分之五十几率+现金20000，百分之五十-现金10000"""
#     n = random.randint(1,10)
#     if n <= 5:
#         player.cash += 20000
#         player.money += 20000
#         print("恭喜你，中奖啦！现金+20000")
#     else:
#         player.cash -= 10000
#         player.money -= 10000
#         print("恭喜你，中奖啦！现金-10000")
#     player.Luck_card -= 1
#
# def HouseBuild(map,player):
#     '''建房卡'''
#     map.price = 0
#     buy(player,map)
#     self.House_Build -= 1
#
# def StagnantCard(player):
#     '''停滞一回合卡'''
#     pass
#
#
#
#
# player1 = Player('张三')
# player1.show()
# # HouseBuild(map,player1)
# LuckCard(player1)
# print('-'*20)
# player1.show()


