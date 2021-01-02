import sys
r=sys.stdin.readline
def revAndnot(bit,idx):
    tmp=""
    for i in range(idx):
        tmp+='1' if bit[i]=='0' else '0'
    return tmp[::-1]+bit[idx:]
for _ in range(int(r())):
    n=int(r())  #length of binary
    a=r().strip()
    b=r().strip()
    ans=[]
    for i in range(n):
        if a[i]!=b[i]:
            if i>0:
                ans.append(str(i+1))
            ans.append('1')
            if i>0:
                ans.append(str(i+1))
    print(len(ans),end=" ")
    print(' '.join(ans))