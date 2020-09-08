import sys
from collections import defaultdict
r=sys.stdin.readline
S=r().strip()
words=defaultdict(list)
for _ in range(int(r())):
    tmp=r().strip()
    words[S.find(tmp)]+=len(tmp)
flg=False
for item in words[0]:
    cur=item
    while True:
        if words[cur+1]==[]:
            break
        else:
            

