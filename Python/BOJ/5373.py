import sys
#from copy import deepcopy
r=sys.stdin.readline
class Cube(): 
    def __init__(self):
        self.U=[['w']*3 for _ in range(3)]
        self.D=[['y']*3 for _ in range(3)]
        self.F=[['r']*3 for _ in range(3)]
        self.B=[['o']*3 for _ in range(3)]
        self.L=[['g']*3 for _ in range(3)]
        self.R=[['b']*3 for _ in range(3)]
        self.tb={
            ('U','+'):[self.B,self.R,self.F,self.L],
            ('U','-'):[self.B,self.L,self.F,self.R],
            ('D','+'):[self.B,self.L,self.F,self.R],
            ('D','-'):[self.B,self.R,self.F,self.L],
            ('F','+'):[self.U,self.L,self.D,self.R],
            ('F','-'):[self.U,self.R,self.D,self.L],
            ('B','+'):[self.U,self.R,self.D,self.L],
            ('B','-'):[self.U,self.L,self.D,self.R],
            ('L','+'):[self.U,self.B,self.D,self.F],
            ('L','-'):[self.U,self.F,self.D,self.B],
            ('R','+'):[self.U,self.F,self.D,self.B],
            ('R','-'):[self.U,self.B,self.D,self.F]
        }    
    def vertical(self,target):
        return [[target[j][i] for j in range(3)] for i in range(3)]
    def up(self,target,colors):
        target[2]=list(colors)
    def down(self,target,colors):
        target[0]=list(colors)
    def left(self,target,colors):
        tmp=self.vertical(target)
        tmp[2]=colors
        target=self.vertical(tmp)
    def right(self,target,colors):
        tmp=self.vertical(target)
        tmp[0]=colors
        target=self.vertical(tmp)

    def rotate(self,base,direction):
        lst=self.tb[(base,direction)]
        tmp=[]
        for i in range(4):
            if i==0:
                tmp.append(lst[i][2])
            if i==1:
                tmp2=self.vertical(lst[i])
                if direction=='+':
                    tmp.append(tmp2[2])
                else:
                    tmp.append(tmp2[0])
            if i==2:
                tmp.append(lst[i][0])
            if i==3:
                tmp2=self.vertical(lst[i])
                if direction=='+':
                    tmp.append(tmp2[0])
                else:
                    tmp.append(tmp2[2])
        
        self.up(lst[0],tmp[1])
        self.right(lst[1],tmp[2])
        self.down(lst[2],tmp[3])
        self.left(lst[3],tmp[0])

for _ in range(int(r())):
    n=int(r())
    op_lst=list(r().split())
    cube=Cube()
    for op in op_lst:
        cube.rotate(op[0],op[1])
    for line in cube.U:
        print(''.join(line))