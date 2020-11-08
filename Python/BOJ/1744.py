import sys
r=sys.stdin.readline
N=int(r())
zero=[]
pos=[]
neg=[]
for _ in range(N):
    tmp=int(r())
    if tmp>0: pos.append(tmp)
    elif tmp==0: zero.append(tmp)
    else: neg.append(tmp)
ans=0

if len(neg)>1:
    neg.sort(reverse=True)
    while len(neg)>1:
        a=neg.pop()
        b=neg.pop()
        ans+=(a*b)
    if neg:
        ans+=neg[0]
elif len(neg)==1:
    