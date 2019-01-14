import throw

#回合开始初始化玩家位置
player1=(x,y)
player2=(a,b)
#判定前需要一个容器分别记录玩家购买建筑的位置坐标
player1_building = []
player2_building = []
class Gamelogic:
    def __init__(self,dice,money):
        self.dice=dice
        self.money = money
    
        
   #根据骰子点数前进
    def move(self):
        #判定当前位置坐标,决定横坐标或纵
        #坐标加x单位距离,得出新位置坐标
        #返回值为新位置坐标(元组)
        if count(dice) %2 != 0:
            x += self.dice[0]
            y += self.dice[1]
            player1 = (x,y)
            return player1
        else:
            a += self.dice[0]
            b += self.dice[1]
            player2 = (a,b)
            return player2

    #落点归属判定
    def affiliation():
        # 如果玩家所到此处位置为空地,则不做任何操作
        # place_building共有三种状态:no building,true,false
        if place_building == "no building":
            pass
        #此处建筑为可购买状态 
        elif place_building == "ture":
            # 玩家的金币大于购买建筑金币数
            if player_money >= buybuilding_money:
                # 询问是否需要购买该建筑
                need_buy_building = input("是否购买该建筑?")
                # 此处应为弹框显示事件,这里省略
                if need_buy_building == "是":
                    # 扣除买建筑所需的金币,转换该建筑可购买状态
                    # 为false,此处建筑物等级加一,
                    # 过路费有一定的规则函数单独写出,
                    # 此处不做列举
                    player_money -= buybuilding_money
                    place_building_ = false
                    place_
                else:
                    # 玩家不购买
                    # 点击事件,此处省略
                    pass  #进入下一回合
    
    # 过路费规则
    # 当玩家所处位置为对方已购买的建筑地点时调用
    # 玩家创建的房屋（不考虑添加加盖卡）：第一次占地2400(电脑经过收入1400),
    # 第二次240（电脑经过收入）
    # 		第三次升级1200
    # 	1级住宅付6400 2级住宅付12000 3级付24000
    def tools():
        # 定义购买状态为false的建筑物们的等级状态
        if 


# 定义建筑物的属性,怎么设置三种建筑物状态
# 用列表存储?还是用直接赋值,直接用变量接收吧,用变量接收后又从哪里存储数据,
# 如何调用该属性
class Place_Building():
    def __init__(self):
        pass
        # 定义建筑物可购买状态
    def states():
        






    


    



