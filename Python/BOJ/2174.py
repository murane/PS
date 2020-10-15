import sys
r=sys.stdin.readline
A,B=map(int,r().split())
N,M=map(int,r().split())
#N개의 로봇 M개의 명령
#가로A 세로B
land=[[0]*A for _ in range(B)]
robots={}
tb={'N':(-1,0),'W':(0,-1),'S':(1,0),'E':(0,1)}
for i in range(1,N+1):
    s=r().split()
    x,y,d=int(s[0])-1,int(s[1]),s[2]
    land[B-y][x]=[i,d]
    robots[i]=[B-y,x,d]
lst=[]
for _ in range(M):
    s=r().split()
    num,op,times=int(s[0]),s[1],int(s[2])
    lst.append([num,op,times])
for num,op,times in lst:
    while times>0:
        i=num
        if op=='F':
            Nx,Ny=robots[i][1]+tb[robots[i][2]][1],robots[i][0]+tb[robots[i][2]][0]
            d=land[robots[i][0]][robots[i][1]][1]
            if 0<=Ny<=B-1 and 0<=Nx<=A-1:
                if land[Ny][Nx]==0:
                    land[robots[i][0]][robots[i][1]]=0
                    robots[i]=[Ny,Nx,d]
                    land[Ny][Nx]=[i,d]
                else:
                    print(f'Robot {i} crashes into robot {land[Ny][Nx][0]}')
                    exit(0)
            else:
                print(f'Robot {i} crashes into the wall')
                exit(0)
        elif op=='L':
            if robots[i][2]=='N':robots[i][2]='W'
            elif robots[i][2]=='E':robots[i][2]='N'
            elif robots[i][2]=='W':robots[i][2]='S'
            elif robots[i][2]=='S':robots[i][2]='E'
            land[robots[i][0]][robots[i][1]][1]=robots[i][2]
        elif op=='R':
            if robots[i][2]=='N':robots[i][2]='E'
            elif robots[i][2]=='E':robots[i][2]='S'
            elif robots[i][2]=='W':robots[i][2]='N'
            elif robots[i][2]=='S':robots[i][2]='W'
            land[robots[i][0]][robots[i][1]][1]=robots[i][2]
        times-=1
print("OK")