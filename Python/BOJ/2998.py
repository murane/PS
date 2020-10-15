import sys
r=sys.stdin.readline
binStr=r().strip()
if len(binStr)%3==1:
    binStr= '00'+binStr
elif len(binStr)%3==2:
    binStr= '0'+binStr
res=''
tmp=''
while binStr!='':
    tmp+=binStr[0]
    binStr=binStr[1:]
    if len(tmp)==3:
        res+=(str(int(tmp,2)))
        tmp=''
        continue
print(res)