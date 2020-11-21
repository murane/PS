import sys
from itertools import combinations
r = sys.stdin.readline
N = int(r())
edge = dict()
ans=set()
mx = 0

def get_xy_z(xyz:list):
    lst=[]
    for i in range(3):
        tmp=xyz.pop(i)
        xyz.sort()
        lst.append((tuple(xyz),tmp))
    lst=list(set(lst))
    return lst

for i in range(1, N + 1):
    xyz = list(map(int, r().split()))
    ans.add((min(xyz), i))
    
    xy_z=get_xy_z(xyz)

    for pair,z in xy_z:
        if pair not in edge:
            edge[pair]=(z,i)
        else:
            c,idx=edge[pair]
            edge[pair]=(c,idx) if c>z else (z,i)
            lst=list(pair)+[c+z]
            tmp=max(mx,min(lst))
            mx=(tmp, (idx,i))

ans=list(ans)
ans.sort(key=lambda x: x[0])
if ans[0][0]>mx[0]:
    print(ans[0][0])
    print(ans[0][1])
else:
    print(mx[0])
    print(*mx[1])