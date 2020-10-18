import sys
r=sys.stdin.readline
N=int(r())
cities=[]
for _ in range(N):
    x,y,z=map(int,r().split())
    cities.append((x,y,z))

tb=[]
dp('000')