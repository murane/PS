import sys
r=sys.stdin.readline
S=list(r().strip())
ans=S[0]
def calc(a,b):
    a,b=int(a),int(b)
    if a<=1 or b<=1:
        return a+b
    else: return a*b
for i in range(1,len(S)):
    ans=calc(ans,S[i])
print(ans)

