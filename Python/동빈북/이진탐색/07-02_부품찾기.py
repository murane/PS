import sys
r=sys.stdin.readline
N=int(r())
parts=list(map(int,r().split()))
partsSet=set(parts)
M=int(r())
query=list(map(int,r().split()))
res=["YES" if x in partsSet else "NO" for x in query]
print(" ".join(res))