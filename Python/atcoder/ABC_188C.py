import sys
r=sys.stdin.readline
N=int(r())
A=list(map(int,r().split()))
lst=[]
for i in range(2**N):
    lst.append((i+1,A[i]))
while len(lst)>2:
    tmp=[]
    for i in range(1,len(lst)//2+1):
        if lst[2*i-2][1]>lst[2*i-1][1]:
            tmp.append(lst[2*i-2])
        else:
            tmp.append(lst[2*i-1])
    lst=tmp
if lst[0][1]>lst[1][1]:
    print(lst[1][0])
else:
    print(lst[0][0])