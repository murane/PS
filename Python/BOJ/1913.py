import sys,math
r=sys.stdin.readline
N=int(r())
n=int(r())
tb=[[-1,0],[0,1],[1,0],[0,-1]]#위 오른쪽 아래 왼쪽
def buildSnail(N):#
    snail=[[0]*N for _ in range(N)]         #달팽이 배열 N*N
    curPos=[math.floor(N/2),math.floor(N/2)]  #홀수만들어오니까 가운데 좌표설정
    curDire=0                               #방향은 위부터
    curnum=1                                #1부터 시작
    snail[curPos[0]][curPos[1]]=curnum      #초기좌표설정
    curCnt=1                                #반복횟수
    while True:
        for _ in range(2):
            for _ in range(curCnt):
                curnum+=1
                curPos[0]+=tb[curDire][0]
                curPos[1]+=tb[curDire][1]
                snail[curPos[0]][curPos[1]]=curnum
                if curnum==N**2:
                    return snail
            curDire=(curDire+1)%4
        curCnt+=1
snail=buildSnail(N)
pos=[]
for i in range(len(snail)):
    for j in range(len(snail[0])):
        print(snail[i][j],end=" ")
        if snail[i][j]==n:
            pos.extend([i+1,j+1])
    print("")
print(*pos)