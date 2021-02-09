import sys
r=sys.stdin.readline
N,S=map(int,r().split())
arr=list(map(int,r().split()))
ans=[]
s,e=0,1
tmp=arr[0]
while True:
    if tmp>=S:
        ans.append(e-s)
        tmp-=arr[s]
        s+=1
    elif e==N:
        break
    elif tmp<S:
        tmp+=arr[e]
        e+=1           
if ans:
    print(min(ans))
else:
    print(0)
