import sys
from collections import Counter
r=sys.stdin.readline
word=""
cnt=0
for i in range(int(r())):
    if i==0:
        word=list(r().strip())
        word=Counter(word)
    else:
        tmp=Counter(r().strip())
        a,b=word-tmp,tmp-word
        if len(a.items())>1 or len(b.items())>1:
            continue
        if len(a.items())==1 and list(a.items())[0][1]>1:
            continue
        if len(b.items())==1 and list(b.items())[0][1]>1:
            continue
        cnt+=1
print(cnt)
        
