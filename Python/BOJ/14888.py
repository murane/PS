import sys
from itertools import permutations
r = sys.stdin.readline
MAX=1000000000
MIN=-1000000000
N=int(r())
numbers = list(map(int,r().split()))
operands = list(map(int,r().split()))
ops=[]
for i in range(len(operands)):
    for j in range(operands[i]):
        if i==0:
            ops.append('+')
        elif i==1:
            ops.append('-')
        elif i==2:
            ops.append('*')
        elif i==3:
            ops.append('/')
op_list = permutations(ops,len(ops))
res=[]
for op_order in op_list:
    temp=0
    for i in range(len(numbers)):
        if i==0:
            tmp=numbers[i]
        else:
            if op_order[i-1]=='+':
                temp=tmp+numbers[i]
            elif op_order[i-1]=='-':
                temp=tmp-numbers[i]
            elif op_order[i-1]=='*':
                temp=tmp*numbers[i]
            elif op_order[i-1]=='/':
                temp=int(tmp/numbers[i])
            tmp=temp
    if temp>MAX:
        temp=MAX
    elif temp<MIN:
        temp=MIN
    res.append(temp)
print(max(res))
print(min(res))