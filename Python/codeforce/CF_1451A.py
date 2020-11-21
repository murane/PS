import sys
r=sys.stdin.readline
for _ in range(int(r())):
    n=int(r())
    ans=0
    while True:
        if n==1:
            break
        elif n==2 or n%2==1:
            n-=1
            ans+=1
        else:
            n=n//(n//2)
            ans+=1
    print(ans)