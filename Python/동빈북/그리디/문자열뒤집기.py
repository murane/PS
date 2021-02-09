import sys
r=sys.stdin.readline
S=r().strip()
zero,one=0,0
prev=-1
for num in S:
    if prev==-1:
        if num=='1':one+=1
        else:zero+=1
    else:
        if num!=prev:
            if num=='1':one+=1
            else:zero+=1
    prev=num
print(min(zero,one))