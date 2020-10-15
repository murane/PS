import sys
r=sys.stdin.readline
S=r().strip()
Tag=False
tmp=""
res=""
for i,ch in enumerate(S):
    if ch=="<":
        if tmp!="":
            res+=tmp[::-1]
            tmp=""
        Tag=True
        tmp+=ch
    elif ch==">":
        tmp+=ch
        res+=tmp
        tmp=""
        Tag=False
    elif ch==" ":
        if Tag:
            tmp+=ch
        else:
            res+=(tmp[::-1]+ch)
            tmp=""
    else:
        tmp+=ch
        if i==len(S)-1:
            res+=tmp[::-1]
print(res)