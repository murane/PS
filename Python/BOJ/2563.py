import sys
r=sys.stdin.readline
dohwaji=[[0]*100 for _ in range(100)]
def coloring(x,y):
    for i in range(x,x+10):
        for j in range(y,y+10):
            dohwaji[i][j]=1
for _ in range(int(r())):
    x,y=map(int, r().split())
    coloring(x-1,y-1)
area=0
for i in range(100):
    for j in range(100):
        if dohwaji[i][j]==1:
            area+=1
print(area)