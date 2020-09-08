import sys
from collections import Counter
r=sys.stdin.readline
N=int(r())
numbers=list(map(int,r().split()))
M=int(r())
howmany=list(map(int,r().split()))
"""
num_dict={}
for num in numbers:
    try:
        num_dict[num]+=1
    except:
        num_dict[num]=1
for num in howmany:
    try:
        print(num_dict[num],end=" ")
    except:
        print("0",end=" ")
"""
counter=Counter(numbers)
print(" ".join(str(counter[x]) for x in howmany))

