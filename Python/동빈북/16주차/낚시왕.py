import sys
read=sys.stdin.readline
#100*100 격자
R,C,M=map(int,read().split())
sharkCol=[dict() for _ in range(C)]
di={1:(-1,0),2:(1,0),3:(0,1),4:(0,-1)}
for _ in range(M):
    r,c,s,d,z=map(int,read().split())
    sharkCol[c-1][r-1]=(s,d,z)
ans=0
col=-1
def move():
    removeDict=dict()
    
    for col,colDict in enumerate(sharkCol):
        for row,v in colDict.items():
            s,d,z=v
            x,y=row,col
            dire=di[d]
            nx,ny=(x+dire[0]*s)%R,(y+dire[1]*s)%C
            if nx in sharkCol[ny]:
                if sharkCol[ny][nx][2]<z:
                    sharkCol[ny][nx]=v
            else:
                sharkCol[ny][nx]=v
            removeDict[(x,y)]=v
    for k,v in removeDict.items():
        sharkCol[k[1]].pop(k[0])
def catch(col):
    row=sorted(sharkCol[col].keys())[0]
    _,_,z=sharkCol[col][row]
    sharkCol[col].pop(row)
    return z
while col<C:
    col+=1
    ans+=catch(col)
    move()
print(ans)
