import sys
r=sys.stdin.readline
from itertools import combinations

def calc(pos):
    memory=[]
    operator="+-*"
    bracket=(False,-1)
    for i,v in enumerate(expression):   
        if bracket[0]==True:
            if v in operator:
                bracket=(True,bracket[1]+v)
            else:
                memory.append(str(eval(bracket[1]+v)))
                bracket=(False,-1)
            if len(memory)==3:
                memory[0]=str(eval(''.join(memory)))
                memory=memory[:1]
            continue
        if str(i//2) in pos and i%2==0:
            bracket=(True,v)
        else:
            memory.append(v)
        if len(memory)==3:
            memory[0]=str(eval(''.join(memory)))
            memory=memory[:1]
    return int(memory[0])
N=int(r())
expression=r().strip()
if N==1:
    print(int(expression))
    exit(0)
bracket_pos=[]
num_of_operand=N//2+1
operand_pos=list(range(num_of_operand-1))
for num in range(1,(num_of_operand-1)//2+2):
    valid_pos=[]
    for pos in combinations(map(str,operand_pos),num):
        if [int(pos[i+1])-int(pos[i]) for i in range(len(pos)-1)].count(1)>0:
            continue
        else:
            valid_pos.append(pos)
    bracket_pos.extend(valid_pos)
res = list(map(calc,bracket_pos))
print(max(res))
