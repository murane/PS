import sys
from itertools import product
r=sys.stdin.readline
expression=r().strip()
stack=[]
bracket=[]
res=[]
def indexToDel(s:str,index:int)->str:
    return s[:index]+s[index+1:]
for i,ch in enumerate(expression):
    if ch=='(':
        stack.append(i)
    elif ch==')':
        bracket.append((stack.pop(),i))
for seq in list(product([0,1],repeat=len(bracket))):
    tmp=expression[:]
    for i,x in enumerate(seq):
        if x==0:
            tmp=indexToDel(tmp,bracket[i][0])
            tmp=indexToDel(tmp,bracket[i][1]-1)
    res.append(tmp)
res.sort()
print('\n'.join(res))