import sys
class Dice:
    def __init__(self):
        self.plane=[0,0,0,0,0,0]
        self.table={
            (1,'N'):5,(1,'S'):2,(1,'W'):3,(1,'E'):4,
            (2,'N'):1,(2,'S'):6,(2,'W'):3,(2,'E'):4,
            (3,'N'):5,(3,'S'):2,(3,'W'):6,(3,'E'):1,
            (4,'N'):5,(4,'S'):2,(4,'W'):1,(4,'E'):6,
            (5,'N'):6,(5,'S'):1,(5,'W'):3,(5,'E'):4,
            (6,'N'):2,(6,'S'):5,(6,'W'):3,(6,'E'):4,
        }
        self.di={
            1:'E',2:'W',3:'N',4:'S'
        }
        self.updown={
            1:6,2:5,3:4,4:3,5:2,6:1
        }
        self.top=1
        self.bottom=6
    def move(self, direction, num):
        self.top = self.table[(self.top,self.di[direction])]
        self.bottom = self.updown[self.top]
        self.plane[self.bottom-1]=num


r=sys.stdin.readline
N,M,x,y,K=list(map(int,r().split()))
coords=[]
for _ in range(N):
    tmp = list(map(int,r().split()))
    coords.append(tmp)
commands=list(map(int,r().split()))
dice=Dice()
x,y=y,x
cur=coords[x][y]
for comm in commands:
    if (comm==1 and y==M-1) or (comm==2 and y==0) or (comm==3 and x==0) or (comm==4 and x==N-1):
        continue
    else:
        if comm==1:
            y+=1
        elif comm==2:
            y-=1
        elif comm==3:
            x-=1
        elif comm==4:
            x+=1
        
        cur=coords[x][y]
        dice.move(comm,cur)
        print(dice.plane[dice.top-1])
    
    
