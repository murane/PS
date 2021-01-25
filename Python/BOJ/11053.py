import sys
r=sys.stdin.readline
N=int(r())
seq=list(map(int,r().split()))
ans=0
for i in range(len(seq)):
    tmp=[]
    for j in range(i,len(seq)):
        if not tmp:
            tmp.append(seq[j])
        elif tmp[-1]<seq[j]:
            tmp.append(seq[j])
    ans=max(ans,len(tmp))
print(ans)
