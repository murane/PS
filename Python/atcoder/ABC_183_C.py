import sys
r=sys.stdin.readline
N,K=map(int,r().split())
city=[]
for _ in range(N):
    city.append(list(map(int,r().split())))
res=[]
def travel(cur,visit,cost):
    if visit==(1<<N)-1:
        res.append(cost+city[cur][0])
    for i,nextC in enumerate(city[cur]):
        if nextC!=0 and not visit&(1<<i):
            travel(i,visit|(1<<i),city[cur][i]+cost)
travel(0,1<<0,0)
print(len(list(filter(lambda x: x==K,res))))