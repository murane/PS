import sys
r=sys.stdin.readline
A,B,C=map(int,r().split())
_bin=bin(B)[2:]
res=1
tmp=1
for i,num in enumerate(_bin[::-1]):
    if i==0:
        tmp=A%C
    else:
        tmp=(tmp**2)%C
    if num=='1':
        res*=tmp
print(res%C)
