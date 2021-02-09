from collections import defaultdict,deque
def solution(n, edges):
    if len(edges)==2:
        return 1
    g=defaultdict(list)
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)
    nodes,_=bfs(g,1,n)
    if len(nodes)==1:
        nodes,dist=bfs(g,nodes[0],n)
        if len(nodes)==1:
            return dist-1
        else:
            return dist
    else:
        
    node2,dist=bfs(g,nodes[0],n)
    if cnt>1:
        return dist
    else:
        return dist-1

def bfs(graph,node,n):
    visited=[False]*(n+1)
    dist=[-1]*(n+1)
    dist[node]=0
    q=deque([node])
    visited[node]=True
    while q:
        cur=q.popleft()
        for i in graph[cur]:
            if not visited[i]:
                visited[i]=True
                dist[i]=dist[cur]+1
                q.append(i)
    maxDist=0
    lst=[]
    for i in range(1,n+1):
        if dist[i]>maxDist:
            lst=[i]
            maxDist=dist[i]
            idx=i
        if dist[i]==maxDist:
            lst.append(i)

    return lst,maxDist
if __name__ == '__main__':
    
    print(solution(arr))
