import sys
from collections import Counter
r = sys.stdin.readline
def is_p(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
N = int(r())
nums = list(map(int,r().split()))
print(Counter(list(map(is_p, nums)))[True])
