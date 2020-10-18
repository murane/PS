import sys
r=sys.stdin.readline
N,M=map(int,r().split())
s=[list(r().strip()) for _ in range(N)]
def find(x,y,leng):
    a=(x,y)
    b=(x+leng-1,y)
    c=(x,y+leng-1)
    d=(x+leng-1,y+leng-1)
    if s[a[0]][a[1]]==s[b[0]][b[1]]==s[c[0]][c[1]]==s[d[0]][d[1]]:
        return True
    else:
        return False

tmp=min(N,M)
ans=1
if tmp==1:
    print(1)
    exit(0)
for x in range(2,tmp+1):
    for i in range(N-x+1):
        for j in range(M-x+1):
            if find(i,j,x):
                ans=x**2
print(ans)
    