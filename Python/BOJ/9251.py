import sys
r=sys.stdin.readline
A=r().strip()
B=r().strip()
dp=[[-1]*len(B) for _ in range(len(A))]
dp[0][0]=0

