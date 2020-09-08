import sys
from collections import defaultdict
r=sys.stdin.readline
N=int(r())
word=defaultdict(list)
save=[]
def fuck(word)->list:
    res=[]
    for i in range(len(word)-1):
        res.append(word[:i+1])
        res.append(word[-(i+1):])
    return res
for _ in range(N*2-2):
    tmp=r().strip()
    save.append(tmp)
    word[len(tmp)].append(tmp)
if N==2:
    print(save[0]+save[1])
    print("PS")
    exit(0)
a,b=word[N-1][0],word[N-1][1]
S=""
if sorted(fuck(b[:]+a[-1]))==sorted(save):
    S=b[:]+a[-1]
else:
    S=a[:]+b[-1]
res=""
tmp2=defaultdict(bool)
for i in save:
    if S.find(i)==0 and not tmp2[len(i)]:
        res+="P"
        tmp2[len(i)]=True
    else:
        res+="S"
print(S)
print(res)