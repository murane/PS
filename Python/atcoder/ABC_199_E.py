import sys,math
r=sys.stdin.readline
N,M=map(int,r().split())

#1~N까지의 정수 순열중에서
#1~Xi까지의 수열중 최대 Zi개의 수가 Yi보다 작거나 같다
print(math.factorial(N))