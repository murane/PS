import sys
from collections import deque
import heapq
r=sys.stdin.readline
N,K=map(int,r().split())
visit=[-1]*100001

def bfs(cur):
    q=deque()
    q.append(cur)
    if K==cur: return 0
    heap=[]
    heapq.heappush(heap,(0,cur))
    while q:
        dist,pos=heapq.heappop(heap)
        if visit[pos]!=-1: continue
        visit[pos]=dist
        for i,Npos in enumerate([pos*2,pos+1,pos-1]):
            if 0<=Npos<=100000:
                if i==0:
                    heapq.heappush(heap,(dist,Npos))
                    if K==Npos: return dist
                else:
                    heapq.heappush(heap,(dist+1,Npos))
                    if K==Npos: return dist+1

print(bfs(N))