import sys
from collections import Counter
from itertools import permutations
r=sys.stdin.readline
def game(num,candi):
    s,b=0,0
    for a,b in zip(str(num),str(candi)):
        if a==b:
            s+=1
        elif num[i] in candi:
            b+=1
    return s,b
candidates=[]
for i in range(1,10-2):
    for j in range(i+1,10-1):
        for k in range(j+1,10):
            for perm in permutations(str(i)+str(j)+str(k),3):
                candidates.append(int(''.join(perm)))
for _ in range(int(r())):
    num,s,b=map(int,r().split())
    res=[]
    for candi in candidates:
        if game(num,candi) == (s,b):
            res.append(candi)
    candidates=res
print(len(candidates))