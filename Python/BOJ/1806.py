import sys
r=sys.stdin.readline
N,S=map(int,r().split())
candi_arr=[]
arr=list(map(int,r().split()))
s,e=0,0
tmp=0
while s<len(arr) and e<len(arr):
    if s==0 and e==0:
        tmp=arr[0]
        e+=1
    else:
        if tmp<S:
            tmp+=arr[e]
            e+=1
        elif tmp>S:
            tmp-=arr[s]
            s+=1
        else:
            candi_arr.append(e-s+1)
if not candi_arr:
    print(0)
else:
    print(min(candi_arr))