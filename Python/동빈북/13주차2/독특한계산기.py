import sys
from collections import deque
r=sys.stdin.readline
exp=r().strip()
expQ=deque()
buf=""
minus=False
op="+-*/"
if exp.startswith("-"):
    exp=exp[1:]
    minus=True
for i,ch in enumerate(exp):
    if buf!="":
        if ch in op:
            expQ.append(buf)
            expQ.append(ch)
            buf=""
        else:
            buf+=ch
    else:
        buf+=ch
    if i==len(exp)-1:
        expQ.append(buf)
opDict={'+':1,'-':1,'*':2,'/':2}
if minus:
    expQ[0]='-'+expQ[0]
def left3(lvl):
    for _ in range(3):
        expQ.popleft()
    expQ.appendleft(lvl)
def right3(rvl):
    for _ in range(3):
        expQ.pop()
    expQ.append(rvl)
def eval(l,op,r):
    l,r=int(l),int(r)
    if op=='+':
        return l+r
    if op=='-':
        return l-r
    if op=='*':
        return l*r
    if op=='/':
        return int(l/r)
def calc():
    ln1,lop,ln2=expQ[0],expQ[1],expQ[2]
    rn1,rop,rn2=expQ[-3],expQ[-2],expQ[-1]
    lvl=eval(ln1,lop,ln2)
    rvl=eval(rn1,rop,rn2)
    if opDict[lop]>opDict[rop]:
        left3(lvl)
    elif opDict[lop]<opDict[rop]:
        right3(rvl)
    else:
        if lvl>rvl:
            left3(lvl)
        elif lvl<rvl:
            right3(rvl)
        else:
            left3(lvl)
while len(expQ)>1:
    calc()
print(int(expQ[0]))
        