import sys
from collections import defaultdict
r=sys.stdin.readline
N,M=map(int,r().split())
res=""
def hamDist(dna1:str, dna2:str):
    cnt=0
    for i in range(len(dna1)):
        if dna1[i]!=dna2[i]:
            cnt+=1
    return cnt
DNA_lst=[]
for _ in range(N):
    DNA_lst.append(r().strip())
for i in range(len(DNA_lst[0])):
    DNA_dict=defaultdict(int)
    for j in range(len(DNA_lst)):
        DNA_dict[DNA_lst[j][i]]+=1
    tmp=["",0]
    for k in sorted(DNA_dict.keys()):
        if DNA_dict[k]>tmp[1]:
            tmp[0]=k
            tmp[1]=DNA_dict[k]
    res+=tmp[0]
print(res)
acc=0
for DNA in DNA_lst:
    acc+=hamDist(DNA,res)
print(acc)