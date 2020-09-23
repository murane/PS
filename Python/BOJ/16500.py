import sys
r=sys.stdin.readline
S=r().strip()
words=[]
for _ in range(int(r())):
    words.append(r().strip())
dp=[-1]*101

def solve(pos):
    if pos==len(S):
        return 1
    ret=dp[pos]
    if ret!=-1:
        return ret
    ret=0

    for word in words:
        if len(S)-pos<len(word):
            continue
        if S.find(word,pos,pos+len(word))!=-1:
            ret=ret+solve(pos+len(word)) 

    if ret>0:
        ret=1
    dp[pos]=ret
    return dp[pos]

print(solve(0))