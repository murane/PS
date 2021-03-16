import sys
from collections import defaultdict
r=sys.stdin.readline
N=int(r())
class Trie:
    def __init__(self):
        self.node = dict()
    def insert(self, lst:list):
        currentNode = self.node
        for item in lst:
            if item not in currentNode:
                currentNode[item]=dict()
            currentNode=currentNode[item]

    def sol(self):
        self.recur(self.node,1)

    def recur(self,target,depth):
        for k in sorted(target.keys()):
            print(f'{"--"*(depth-1)}{k}')
            if target[k]!=dict():
                self.recur(target[k],depth+1)

trie = Trie()
for _ in range(N):
    line = list(r().split())
    trie.insert(line[1:])

trie.sol()