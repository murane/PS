import sys
r=sys.stdin.readline
read=sys.stdin.read
M, N= list(map(int,r().split()))
board= read().split()
chess1=[
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
chess2=[
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]
res=[]
for i in range(len(board)-7):
    for j in range(len(board[0])-7):
        tmp1,tmp2=0,0
        for a in range(8):
            for b in range(8):
                if chess1[a][b] !=board[i+a][j+b]:
                    tmp1+=1
                if chess2[a][b] !=board[i+a][j+b]:
                    tmp2+=1
        res.extend([tmp1,tmp2])
print(min(res))