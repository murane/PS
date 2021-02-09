import sys
from itertools import combinations
r=sys.stdin.readline
N,M=map(int,r().split())
city=[]
for _ in range(N):
    city.append(list(map(int,r().split())))
house,chick=[],[]
for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            house.append((i,j))
        elif city[i][j]==2:
            chick.append((i,j))
def get_dist(coord1,coord2):
    return abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])
ans=[]
#1개 ~ M개 까지 치킨집을 고르는 경우
for i in range(1,M+1):
    dist_lst=[]
    #i개의 치킨집을 고르는 경우
    for chicks in combinations(chick,i):
        dist=0
        for house_xy in house:
            ret=list()
            for chick_xy in chicks:
                ret.append(get_dist(house_xy,chick_xy))
            dist+=min(ret)
        dist_lst.append(dist)
    ans.append(min(dist_lst))
print(min(ans))
