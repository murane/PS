import sys
from itertools import permutations
r = sys.stdin.readline
N=int(r())
A=list(map(int,r().split()))
res=[]
op=""
for i,v in enumerate(list(map(int,r().split()))):# + - * /
    if i==0: op+='+'*v
    elif i==1: op+='-'*v
    elif i==2: op+='*'*v
    else: op+='/'*v
def calc(nums,ops):
    start=nums[0]
    for i in range(len(ops)):
        if ops[i]=='+':
            start+=nums[i+1]
        elif ops[i]=='-':
            start-=nums[i+1]
        elif ops[i]=='*':
            start*=nums[i+1]
        elif ops[i]=='/':
            start=int(start/nums[i+1])
    return start
for operators in list(set(permutations(op,len(op)))):
    res.append(calc(A,operators))
print(max(res))
print(min(res))