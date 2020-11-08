import sys
r=sys.stdin.readline
n,m,k=map(int,r().split())
screen=list(map(int,r().split()))
gesture=0
for app in list(map(int,r().split())):
    screen.index(app)
def launch(num):
    num//k