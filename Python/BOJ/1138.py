import sys
r=sys.stdin.readline
N=int(r())
key=list(map(int,r().split()))
ans=[0]*N
for i in range(1,N+1):
    cnt=0
    k=key[i-1]#자신보다 왼쪽에있는 수
    for j in range(0,N):
        if cnt==k and ans[j]==0:#비어있는 자리 + 카운트가 일치할때
            ans[j]=i
            break
        if ans[j]==0:#자리가 비었따면 카운트++
            cnt+=1
print(*ans)


