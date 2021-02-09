def main(f = None):
    input=sys.stdin.readline
    def sol(cur, flag):
        val = cache[cur][flag]
        if val != -1: return val
        val = 0

        if flag:
            val += cost[cur]
            for nxt in tree[cur]:
                val += sol(nxt, 0)
        
        else:
            for nxt in tree[cur]:
                val += max(sol(nxt, 0), sol(nxt, 1))
        cache[cur][flag] = val
        return val

    N = int(input())
    tree = [[] for _ in range(N)]
    cost = [int(i) for i in input().split()]
    parentOf = [None] + [int(i)-1 for i in input().split()]
    for i in range(1, N):
        tree[parentOf[i]].append(i)
    del parentOf
    cache = [[-1]*2 for _ in range(N)]
    
    print(sol(0, 1), sol(0, 0))
    del cost

    def dfs(cur, flag):
        if flag:
            for nxt in tree[cur]:
                dfs(nxt, 0)
        else:
            for nxt in tree[cur]:
                if cache[nxt][0] > cache[nxt][1]:
                    dfs(nxt, 0)
                else:
                    dfs(nxt, 1)
                    lst.append(nxt+1)
    lst = [1]
    dfs(0, 1)
    lst.sort()
    print(*lst, -1)

    lst = []
    dfs(0, 0)
    lst.sort()
    print(*lst, -1)



# CP template Version 1.005
import os
import sys
sys.setrecursionlimit(205000)
import itertools
import collections
from functools import cmp_to_key
from itertools import product
from collections import deque, Counter
from math import log, log2, ceil, floor
import math
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

if __name__ == "__main__":
    main()
