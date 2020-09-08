import sys
from itertools import permutations
r = sys.stdin.readline
N, M = list(map(int,r().split()))


res = list(permutations(range(1,N+1),M))
for item in res:
    for num in item:
        print(num,end=" ")
    print("")
