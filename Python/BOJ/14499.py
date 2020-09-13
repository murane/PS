import sys
class Dice:
    def __init__(self):
        self.D={
            'F':0,'B':0,'L':0,'R':0,'U':0,'D':0
        }
    def move(self,x,y,d):
        if d==1:
            self.D['D'],self.D['R'],self.D['U'],self.D['L']=self.D['R'],self.D['U'],self.D['L'],self.D['D']
        elif d==2:
            self.D['D'],self.D['L'],self.D['U'],self.D['R']=self.D['L'],self.D['U'],self.D['R'],self.D['D']
        elif d==3:
            self.D['F'],self.D['U'],self.D['B'],self.D['D']=self.D['U'],self.D['B'],self.D['D'],self.D['F']
        else:
            self.D['F'],self.D['U'],self.D['B'],self.D['D']=self.D['D'],self.D['F'],self.D['U'],self.D['B']
        if NMmap[x][y]==0:
            NMmap[x][y]=self.D['D']
        else:
            self.D['D']=NMmap[x][y]
            NMmap[x][y]=0
    def up(self):
        return self.D['U']
r=sys.stdin.readline
N,M,x,y,K=list(map(int,r().split()))
NMmap=[]
for _ in range(N):
    tmp = list(map(int,r().split()))
    NMmap.append(tmp)
commands=list(map(int,r().split()))
dice=Dice()
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
        dice.move(x,y,comm)
        print(dice.up())