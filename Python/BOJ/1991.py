import sys
from collections import defaultdict
r=sys.stdin.readline
N=int(r())
tree=defaultdict(list)
for _ in range(N):
    node,L,R=r().split()
    tree[node].extend([L,R])
res1=""
res2=""
res3=""
def traverse(node,type):
    global res1,res2,res3
    L,R=tree[node][0],tree[node][1]
    if type==0:#전위
        res1+=node
        if L!='.': traverse(L,type)
        if R!='.': traverse(R,type)
    elif type==1:#중위
        if L!='.': traverse(L,type)
        res2+=node
        if R!='.': traverse(R,type)
    elif type==2:#후위
        if L!='.': traverse(L,type)
        if R!='.': traverse(R,type)
        res3+=node
traverse('A',0)
traverse('A',1)
traverse('A',2)
print(res1)
print(res2)
print(res3)
