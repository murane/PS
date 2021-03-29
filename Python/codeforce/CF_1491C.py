import sys
rr=sys.stdin.readline

for _ in range(int(rr())):
    n=int(rr())
    S=list(map(int,rr().split()))
    ans=0
    buf=[0]*(n+2)

    for i in range(n):
        #i번째에 들어오는 애
        tmp=buf[i]

        #들어와야할 사람이 더 많으면
        if tmp<S[i]-1:
            #몇명이 추가로 더 필요한지
            ans+=S[i]-1-tmp
            #추가적으로 들어오는 아이 기록
            tmp+=S[i]-1-tmp
        
        buf[i+1]+=tmp-S[i]+1
        for j in range(i+2,min(n,i+S[i]+1)):
            buf[j]+=1
    print(ans)



