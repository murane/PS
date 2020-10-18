import sys
r=sys.stdin.readline
N=int(r())
def md(x,y,a,b):
    return abs(x-a)+abs(y-b)
left_top=(0,0)
left_down=(0,0)
right_top=(0,0)
right_down=(0,0)
for i in range(N):
    x,y = map(int,r().split())
    if i==0:
        left_top=(x,y)
        left_down=(x,y)
        right_top=(x,y)
        right_down=(x,y)
    else:
        if md(0,0,left_down[0],left_down[1])>md(0,0,x,y):
            left_down=(x,y)
        if md(0,0,right_top[0],right_top[1])<md(0,0,x,y):
            right_top=(x,y)
        if right_down[0]-right_down[1]<x-y:
            right_down=(x,y)
        if left_top[1]-left_top[0]<y-x:
            left_top=(x,y)
a=md(left_down[0],left_down[1],right_top[0],right_top[1])
b=md(left_top[0],left_top[1],right_down[0],right_down[1])
print(max([a,b]))