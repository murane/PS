import sys
r=sys.stdin.readline
H,W=map(int,r().split())
blocks=list(map(int,r().split()))
ans=0
pillar=[0,0,0]#idx, height, total
for i,h in enumerate(blocks):
    if pillar[1]==0 and h!=0:#기둥이 처음 생길때
        pillar=[i,h,pillar[2]+0]
    if pillar[1]!=0 and pillar[1]>h: #기둥이 있는데 빗물이 고일때
        