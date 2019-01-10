class player():
    def __init__(self,name,head,pos=(0,0),money=100000):
        self.name = name
        self.name = money
        self.head = head
        self.pos = pos


    def move(self,step):
        for i in range(step):
            if  0 <= self.pos + i < 16:


