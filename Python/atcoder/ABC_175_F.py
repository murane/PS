import sys
from collections import defaultdict

def isPalindrome(string):
    lenStr = len(string)
    for i in range(lenStr/2):
    	if string[i] != string[lenStr-1-i]:
    		return False
    return True

r=sys.stdin.readline
N=int(r())
S=dict()
for _ in range(N):
    word,cost=r().split()
    S[word]=int(cost)

