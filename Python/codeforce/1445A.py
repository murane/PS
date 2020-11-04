import sys
r=sys.stdin.readline
def comp(A:list,B:list)->bool:
    B=list(reversed(B))
    for i in range(len(A)):
        if A[i]+B[i]>x:
            return False
    return True

T=int(r())
for i in range(T):
    n,x=map(int,r().split())
    A=list(map(int,r().split()))
    B=list(map(int,r().split()))
    if comp(A,B):
        print("Yes")
    else:
        print("No")
    if i!=T-1:r()
