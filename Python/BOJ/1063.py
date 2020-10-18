import sys
r=sys.stdin.readline
tmp=r().split()
king,stone,N=tmp[0],tmp[1],int(tmp[2])
chess=[[0]*8 for _ in range(8)]
#chess판에 king과 stone 배치
king=[8-int(king[1]), ord(king[0])-ord('A')]
stone=[8-int(stone[1]), ord(stone[0])-ord('A')]
tb={
    'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),
    'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)
}
for _ in range(N):
    move=r().strip()
    ky,kx=king
    Nky,Nkx=ky+tb[move][0],kx+tb[move][1]
    if 0<=Nky<8 and 0<=Nkx<8:
        sy,sx=stone
        if Nky==sy and Nkx==sx:
            Nsy,Nsx=sy+tb[move][0],sx+tb[move][1]
            if 0<=Nsy<8 and 0<=Nsx<8:
                stone=[Nsy,Nsx]
                king=[Nky,Nkx]
        else:
            king=[Nky,Nkx]
print(chr(king[1]+ord('A'))+str(8-king[0]))
print(chr(stone[1]+ord('A'))+str(8-stone[0]))