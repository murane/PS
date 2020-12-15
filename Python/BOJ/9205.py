import sys
r=sys.stdin.readline
INF=sys.maxsize
def floyd():
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
                    dist[j][i]=dist[i][k]+dist[k][j]
def get_dist(coord_x,coord_y):
    return abs(coord_x[0]-coord_y[0])+abs(coord_x[1]-coord_y[1]) 
    
for _ in range(int(r())):
    n=int(r())
    coords=[]
    for _ in range(n+2):
        coords.append(list(map(int,r().split())))
    dist=[[INF]*(n+2) for _ in range(n+2)]
    for x in range(n+2):
        for y in range(n+2):
            if x==y:
                dist[x][y]=0
            else:
                tmp_dist=get_dist(coords[x],coords[y])
                if tmp_dist>1000:
                    continue
                else:
                    dist[x][y]=tmp_dist
    floyd()
    if dist[0][-1]==INF:
        print("sad")
    else:
        print("happy")
    
