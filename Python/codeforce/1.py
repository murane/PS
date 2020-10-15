import sys
r=sys.stdin.readline
for _ in range(int(r())):
    n=int(r())
    flg=False
    for i in range(n//3+1):
        if flg:
            break
        for j in range((n-3*i)//5+1):
            if flg:
                break
            for k in range((n-3*i-5*j)//7+1):
                if flg:
                    break
                if 3*i+5*j+7*k==n:
                    print(i,j,k)
                    flg=True
    if not flg:
        print(-1)