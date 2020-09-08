import sys
from operator import itemgetter
r=sys.stdin.readline
rr=sys.stdin.readlines
N=int(r())
wordset=set()
for _ in range(N):
    tmp = r().strip()
    wordset.add(tmp)
wordlist=list(wordset)
for i in range(len(wordlist)):
    wordlist[i]=[wordlist[i],len(wordlist[i])]
for word in sorted(wordlist, key=itemgetter(1,0)):
    print(word[0])