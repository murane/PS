import sys
input = sys.stdin.readline

def check():
    dist = [inf]*(N+1)
    dist[1] = 0
    update = False
    for n in range(N):
        update = False
        for s,e,t in adjL:
            if dist[s] + t < dist[e]:
                update = True
                dist[e] = dist[s] + t
        if not update: break
    if update: return True
    return False


inf = 0xfffffff
T = int(input())
for t in range(T):
    N,M,W = map(int,input().split())
    adjL = []
    for m in range(M):
        S,E,T = map(int,input().split())
        adjL.append([S,E,T])
        adjL.append([E,S,T])
    for w in range(W):
        S,E,T = map(int,input().split())
        adjL.append([S,E,-T])

    if check(): print('YES')
    else: print('NO')