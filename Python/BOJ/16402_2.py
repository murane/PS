import sys
r=sys.stdin.readline

def find(x):
    if parent[x]==x:
        return x
    else:
        p=find(parent[x])
        parent[x]=p
        return p
def union(x: int, y: int):#x가 이김...
    _x=find(x)
    _y=find(y)
    if _x!=_y:
        parent[_y]=_x
    else:
        parent[_y]=x
        parent[x]=x

N,M=map(int,r().split())
parent=[]
kingdoms={}
num=0
for _ in range(N):
    kingdom=r().split()[2]
    kingdoms[kingdom]=num
    parent.append(num)
    num+=1

for _ in range(M):
    line=r().strip().split(",")
    former=line[0].split()[2]
    latter=line[1].split()[2]
    winner,loser=0,0
    if line[2]=='1':
        winner,loser=former,latter
    else:
        winner,loser=latter,former
    
    if kingdoms[winner]==find(kingdoms[winner]) and kingdoms[loser]==find(kingdoms[loser]):
        union(kingdoms[winner], kingdoms[loser])
    else:
        #종주국이 속국을 이김
        if kingdoms[winner]==find(kingdoms[winner]) and kingdoms[loser]!=find(kingdoms[loser]):
            #자신의 종주국에 싸움을 건경우
            if find(kingdoms[winner])==find(kingdoms[loser]):
                continue
            else:
                union(kingdoms[winner], kingdoms[loser])
        #속국이 종주국을 이김
        elif kingdoms[winner]!=find(kingdoms[winner]) and kingdoms[loser]==find(kingdoms[loser]):
            if find(kingdoms[winner])==find(kingdoms[loser]):
                union(kingdoms[winner], kingdoms[loser])
            else:
                union(kingdoms[winner], kingdoms[loser])
res=[k for k,v in kingdoms.items() if find(v)==v]
print(len(res))
for name in sorted(res):
    print(f'Kingdom of {name}')