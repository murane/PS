import sys
sys.setrecursionlimit(10**6)
r=sys.stdin.readline
def dfs():
    global cnt
    return cnt

for _ in range(int(r())):
    n=int(r())
    cnt=0
    print(dfs())

        
