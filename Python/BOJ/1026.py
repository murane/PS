import sys
r = sys.stdin.readline
N=int(r())
A=list(map(int,r().split()))
B=list(map(int,r().split()))
A.sort()
B.sort(reverse=True)
sum=0
for i in range(N):
    sum+=(A[i]*B[i])
print(sum)