import sys
r=sys.stdin.readline
N=int(r())
g=[[] for _ in range(N+1)]
selfLst=[]

for i in range(1,N+1):
    g[i].append(int(r()))
    if i==g[i][0]:
        selfLst.append(i)

def dfs(curNode,startNode,leng):
    if leng!=1 and curNode==startNode:
        return leng
    if visit[curNode]:
        return -1
    visit[curNode]=True
    if curNode in selfLst:
        return -1
    return dfs(g[curNode][0],startNode,leng+1)

ans=(0,0)
route=[]
for i in range(1,N+1):
    if i in selfLst:
        continue
    visit=[False]*(N+1)
    tmp=dfs(i,i,1)
    if tmp!=-1:
        ans=(i,tmp)
        route.extend([i for i in range(N+1) if visit[i]])
route=list(set(route))
route.extend(selfLst)
route.sort()
print(len(route))
print('\n'.join(map(str,route)))