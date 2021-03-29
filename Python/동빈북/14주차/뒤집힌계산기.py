import sys
from collections import deque
r=sys.stdin.readline
op="+-*/"
lst=[]
p=list(map(int,r().split()))
pDict={'+':p[0],'-':p[1],'*':p[2],'/':p[3]}
plst=sorted([x for x in pDict.keys()],key=lambda x : -pDict[x])
tmp=""
S=r().strip()
for i,ch in enumerate(S):
    if ch in op:
        lst.append(int(tmp))
        lst.append(ch)
        tmp=""
    else:
        tmp+=ch
        if i==len(S)-1:
            lst.append(int(tmp))

lst=lst[::-1]

def calc(lst,oper):
    q=deque(lst)
    tmp=[]
    while q:
        cur=q.popleft()
        if cur==oper:
            lvl=tmp.pop()
            rvl=q.popleft()
            num=int(eval(str(lvl)+cur+str(rvl)))
            tmp.append(num)
        else:
            tmp.append(cur)
    return tmp
for x in plst:
    lst=calc(lst,x)
print(lst[0])

