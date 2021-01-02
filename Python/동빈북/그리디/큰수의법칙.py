import sys
from collections import Counter
r=sys.stdin.buffer.readline
N,M,K=map(int,r().split())
numbers=list(map(int,r().split()))
counter=Counter(numbers)
cnt_lst=counter.most_common()
cnt_lst.sort(key=lambda x: -x[0])
if cnt_lst[0][1]>1:
    print(cnt_lst[0][0]*M)
else:
    a,b=cnt_lst[0][0],cnt_lst[1][0]
    q,r=divmod(M,K+1)
    print((a*K+b)*q+a*r)
    
