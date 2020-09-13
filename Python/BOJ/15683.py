import sys
from itertools import combinations
r=sys.stdin.readline
N,M=map(int,r().split())
area=[list(map(int,r().split())) for _ in range(N)]
tv=[]
sagak=[]
#CCTV를 스캔하고 각 CCTV의 방향을 정할수 있는 배열 설정

def calcSagak(zone):
    acc=0
    for i in range(len(zone)):
        for j in range(len(zone[0])):
            if zone[i][j]==0:
                acc+=1
    sagak.append(acc)
def printArea(zone):
    for i in range(len(zone)):
        for j in range(len(zone[0])):
            print(zone[i][j],end=" ")
        print("")
def copyArea(area):
    copiedArea=[]
    for i in range(len(area)):
        tmp=[]
        for j in range(len(area[0])):
            tmp.append(area[i][j])
        copiedArea.append(tmp)
    return copiedArea
def reset():
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j]=='#':
                area[i][j]==0
def up(zone,x,y):
    for i in range(x-1,-1,-1):
        if str(zone[i][y]) in "12345#":
            continue
        elif str(zone[i][y])=='6':
            break
        else:
            zone[i][y]="#"

def down(zone,x,y):
    for i in range(x+1,N):
        if str(zone[i][y]) in "12345#":
            continue
        elif str(zone[i][y])=='6':
            break
        else:
            zone[i][y]="#"

def left(zone,x,y):
    for i in range(y-1,-1,-1):
        if str(zone[x][i]) in "12345#":
            continue
        elif str(zone[x][i])=='6':
            break
        else:
            zone[x][i]="#"

def right(zone,x,y):
    for i in range(y+1,M):
        if str(zone[x][i]) in "12345#":
            continue
        elif str(zone[x][i])=='6':
            break
        else:
            zone[x][i]="#"


def monitor(area,index):
    if index==len(tv):
        calcSagak(area)
        #print("---------")
        #printArea(area)
        return
    cctv=tv[index]
    x,y=cctv[0],cctv[1]
    cctv_type=cctv[2]
    if cctv_type==1:
        tmp=copyArea(area)
        up(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)
        down(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)
        left(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)
        right(tmp,x,y)
        monitor(tmp,index+1)
    if cctv_type==2:
        tmp=copyArea(area)
        up(tmp,x,y)
        down(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)
        left(tmp,x,y)
        right(tmp,x,y)
        monitor(tmp,index+1)
    if cctv_type==3:
        tmp=copyArea(area)
        up(tmp,x,y)
        left(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)
        down(tmp,x,y)
        left(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)
        up(tmp,x,y)
        right(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)
        down(tmp,x,y)
        right(tmp,x,y)
        monitor(tmp,index+1)
    if cctv_type==4:
        tmp=copyArea(area)#ㅗ
        up(tmp,x,y)
        left(tmp,x,y)
        right(tmp,x,y)
        monitor(tmp,index+1)#ㅜ
        tmp=copyArea(area)
        down(tmp,x,y)
        left(tmp,x,y)
        right(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)#ㅏ
        up(tmp,x,y)
        down(tmp,x,y)
        right(tmp,x,y)
        monitor(tmp,index+1)
        tmp=copyArea(area)#
        up(tmp,x,y)
        left(tmp,x,y)
        down(tmp,x,y)
        monitor(tmp,index+1)
    if cctv_type==5:
        tmp=copyArea(area)
        up(tmp,x,y)
        down(tmp,x,y)
        left(tmp,x,y)
        right(tmp,x,y)
        monitor(tmp,index+1)


for i in range(len(area)):
    for j in range(len(area[0])):
        if str(area[i][j]) in "12345":
            tv.append((i,j,area[i][j]))

if len(tv)==0:
    calcSagak(area)
    print(min(sagak))
    exit(0)
monitor(area,0)
print(min(sagak))