import sys
from itertools import combinations
from operator import itemgetter
r=sys.stdin.readline
N,M,H=map(int,r().split())
line=set()
for _ in range(M):
    a,b=map(int,r().split())
    line.add((a,b))
def check(lines,pos):
    if pos in lines:
        return False
    if pos[1]>1:
        if (pos[0],pos[1]-1) in lines:
            return False
    if pos[1]<N:
        if (pos[0],pos[1]+1) in lines:
            return False
    return True
def ladderSim(lines:set):
    #lines를 순회하여 arr를 swap했을때 일치하는지를 반환
    arr=list(range(N+1))
    tmp=arr[:]
    #line[0] -> x좌표 line[1] -> y좌표
    lines=list(lines)
    lines.sort(key=itemgetter(0,1))
    for line in lines:
        tmp[line[1]-1],tmp[line[1]]=tmp[line[1]],tmp[line[1]-1]
    if arr==tmp:
        return True
    else:
        return False
def bfs(cur,cnt):
    #가로선 정보를 입력받는다
    #유효한(양옆에 다른 가로선이 있는지)가로선인지 확인한다
    #정답인지 확인한다 -> print and exit
    if cnt==4:
        return
    for i in range(1,H+1):
        for j in range(1,N+1):
            if check(line,(i,j)):
                line.add((i,j))
                if ladderSim(line):
                    print(cnt)
                    exit(0)
                if cur!=cnt:
                    bfs(cur+1,cnt)
                line.remove((i,j))

if M==0 or ladderSim(line):
    print(0)
    exit(0)
else:
    bfs(1,1)
    bfs(1,2)
    bfs(1,3)
print(-1)
