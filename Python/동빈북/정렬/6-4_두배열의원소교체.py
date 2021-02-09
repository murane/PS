import sys
r=sys.stdin.readline
N,K=map(int,r().split())
A=list(map(int,r().split()))
B=list(map(int,r().split()))
A.sort()
B.sort(reverse=True)
for i in range(K):
    if A[i]<B[i]:
        A[i],B[i]=B[i],A[i]
    else:
        break
print(sum(A))