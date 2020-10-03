import sys
r=sys.stdin.readline
N,K=map(int,r().split())
S=r().strip()
def areYourHappy():
    cnt=0
    if len(S)==1:
        return cnt
    for i in range(1,len(S)):
        if S[i-1]==S[i]:
            cnt+=1
    return cnt
def rotate(S,l_idx,r_idx):
    tmp=S[l_idx:r_idx+1]
