import sys
r=sys.stdin.readline
R,C=map(int,r().split())
mokjang=[]
for _ in range(R):
    line=list(r().strip())
    mokjang.append(line)
flg=True
d=[(1,0),(-1,0),(0,1),(0,-1)]
for i in range(R):
    for j in range(C):
        if mokjang[i][j]=="W":
            for k in range(4):
                x,y=i+d[k][0],j+d[k][1]
                if 0<=x<R and 0<=y<C and mokjang[x][y]=='S':
                    print(0)
                    exit(0)
        elif mokjang[i][j]=='.':
            mokjang[i][j]='D'
print(1)
for i in range(R):
    for j in range(C):
        print(mokjang[i][j],end="")
    print()

        
