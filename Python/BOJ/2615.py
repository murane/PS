import sys
r=sys.stdin.readline
board=[list(map(int,r().split()))]
ck=[[[False]*4 for _ in range(19)] for _ in range(19)]
B_cnt=0
W_cnt=0
#가로0 세로 1 좌상~우하2 좌하~우상3
for i in range(20):
    for j in range(20):

def check=(i,j,di):
    start=board[i][j]
    cnt=0
    if ck[i][j][di]:
        return False
    if di==0:
        while 0<=i<20 and 0<=j<20 and board[i][j]==start:
            ck[i][j]=True
            

