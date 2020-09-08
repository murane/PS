import sys
r=sys.stdin.readline
M,N=map(int,r().split())
def vaild_adj(graph: list, v: tuple):
    tmp=[]
    if v[0]!=0 and graph[v[0]-1][v[1]]!=-1:
        tmp.append(graph[v[0]-1][v[1]])
    if v[0]!=len(graph) and graph[v[0]+1][v[1]]!=-1:
        tmp.append(graph[v[0]+1][v[1]])
    if v[1]!=0 and graph[v[0]][v[1]-1]!=-1:
        tmp.append(graph[v[0]][v[1]-1])
    if v[1]!=len(graph[0]) and graph[v[0]][v[1]+1]!=-1:
        tmp.append(graph[v[0]][v[1]+1])
    return tmp
tomato = [list(map(int,r().split())) for _ in range(N)]
