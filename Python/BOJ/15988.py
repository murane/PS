import sys
r=sys.stdin.readline
MOD=10**9+9
tb=[1,2,4]
N=[]
for _ in range(int(r())):
    N.append(int(r()))
for i in range(max(N)-3):
    tb.append((tb[-3]+tb[-2]+tb[-1])%MOD)
for n in N:
    print(tb[n-1])
