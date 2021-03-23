import sys
r=sys.stdin.readline
N,e,w,s,n=map(int,r().split())
total=1
simple=0
d=[(0,1),(0,-1),(1,0),(-1,0)]
prob=[e/100,w/100,s/100,n/100]
visit=set([(0,0)])
def dfs(x,y,level,p):
    if level==0: return p
    tmp=0.0
    for i in range(4):
        Nx,Ny=x+d[i][0],y+d[i][1]
        if (Nx,Ny) not in visit:
            visit.add((Nx,Ny))
            tmp+=dfs(Nx,Ny,level-1,p*prob[i])
            visit.remove((Nx,Ny))
    return tmp
print(dfs(0,0,N,1))
    
