import sys
r=sys.stdin.readline
A,B=map(int,r().split())
m=int(r())
nums=list(map(int,r().split()))
s=0
for i,num in enumerate(reversed(nums)):
    s+=((A**i)*num)
res=[]
while s:
    s,mod=divmod(s,B)
    res.append(mod)
for num in reversed(res):
    print(num,end=" ")
