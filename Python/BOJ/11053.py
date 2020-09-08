import sys
r=sys.stdin.readline
N=int(r())
seq=list(map(int,r().split()))
seqPart=[]
for i in range(len(seq)):
    tmp=[]
    tmp.append(seq[i])
    for j in range(i+1,len(seq)):
        if tmp[-1]<seq[j]:
            tmp.append(seq[j])
    seqPart.append(len(tmp))
print(max(seqPart))
