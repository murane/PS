import sys
r=sys.stdin.readline
N,M=map(int,r().split())
student=list(range(N+1))
def find(X):
    if student[X]==X:
        return X
    student[X]=find(student[X])
    return student[X]
def union(X,Y):
    X=find(X)
    Y=find(Y)
    if X==Y:
        return
    if X>Y:
        student[X]=Y
    else:
        student[Y]=X
for _ in range(M):
    op,a,b=map(int,r().split())
    if op==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")