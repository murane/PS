import sys
r=sys.stdin.readline
Sx,Sy,Gx,Gy=map(int,r().split())
x=(Gx*Sy+Sx*Gy)/(Sy+Gy)
print(f'{x:.10f}')