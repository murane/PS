import sys
from collections import defaultdict
r=sys.stdin.readline
X,Y=map(int,r().split())
#a=X-2b, b=Y-2a
TB=defaultdict(int)
sys.setrecursionlimit(10**6)
TB[(0,1)]=1
TB[(1,0)]=1
if (2*Y-X)%3!=0 or (2*X-Y)%3!=0:
    print(0)
    exit(0)   
a=(2*Y-X)//3
b=(2*X-Y)//3
mod=10**9+7
#permutation with repetition
#ex) ab, ba
def dp(a,b):
    if TB[(a,b)]!=0:
        return TB[(a,b)]
    if a==0 or b==0:
        TB[(a,b)]=1
        return TB[(a,b)]
    else:
        TB[(a,b)]=dp(a-1,b)+dp(a,b-1)
        return TB[(a,b)]
res = dp(a,b)
print(res%mod) 
    
