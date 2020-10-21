import sys
r=sys.stdin.readline
N=int(r())
A=list(map(int,r().split()))
sys.setrecursionlimit(10**6)
_max=-10**9
_min=10**9
operators=map(int,r().split())

def backtrack(res,cnt,limit,plus,minus,mul,div):
    global _max,_min
    if cnt==limit:#연산자를 다뽑아먹음..
        if res>_max:
            _max=res
        if res<_min:
            _min=res
    else:
        if plus:
            backtrack(res+A[cnt+1],cnt+1,limit,plus-1,minus,mul,div)
        if minus:
            backtrack(res-A[cnt+1],cnt+1,limit,plus,minus-1,mul,div)
        if mul:
            backtrack(res*A[cnt+1],cnt+1,limit,plus,minus,mul-1,div)
        if div:
            backtrack(int(res/A[cnt+1]),cnt+1,limit,plus,minus,mul,div-1)

backtrack(A[0],0,N-1,*operators)
print(_max)
print(_min)