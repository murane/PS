import sys
r=sys.stdin.readline
N=int(r())
ans=0
chess=[[False]*N for _ in range(N)]
ck=[-1]*N
colCk=[-1]*N

def backtrack(row):
    global ans
    if row==N:
        ans+=1
        return
    
    for i in range(N):
        if colCk[i]!=-1:continue
        colCk[i]=row
        if canInstall(row,i):
            chess[row][i]=True
            backtrack(row+1) 
            chess[row][i]=False
        colCk[i]=-1

def canInstall(row,col):
    for i in range(N):
        if i==col: continue
        if colCk[i]==-1: continue
        if abs(colCk[i]-row)==abs(i-col):
            return False
    return True
backtrack(0)
print(ans)