import sys
r=sys.stdin.readline
N,K=map(int,r().split())
S=r().strip()
def HappyCnt(S):
    cnt=0
    if len(S)==1:
        return cnt
    for i in range(1,len(S)):
        if S[i-1]==S[i]:
            cnt+=1
    return cnt
def rotate(S,l_idx,r_idx):
    l=S[:l_idx-1]
    if r_idx==len(S):
        r=""
    else:
        r=S[r_idx:]
    tmp=""
    for ch in S[l_idx-1:r_idx:]:
        if ch=="L": tmp+="R"
        elif ch=="R": tmp+="L"
    return l+tmp[::-1]+r
