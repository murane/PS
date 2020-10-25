import sys
from string import digits
r=sys.stdin.readline
S=r().strip()
res=""
stack=[]
tmp=""
level=0
for i,ch in enumerate(S):
    if level>0:#괄호 안에 들어있는 상태
        if ch in digits:
            tmp+=ch
        elif ch=="(":
            level+=1
            mul=tmp[-1]
            tmp=tmp[:-1]
            stack.append((mul,tmp))
            tmp=""
        elif ch==")":
            if level==1:
                mul=stack.pop()
                if mul=="":
                    pass
                else:
                    tmp*=int(mul)
            else:
                mul,prev=stack.pop()
                tmp=(int(mul)*tmp+prev)
            level-=1
            if level==0:
                res+=tmp
    else:#괄호가 없는 상태
        if ch=="(":#괄호를 만남
            level+=1
            if len(tmp)>0:
                stack.append(tmp[-1])
            else:
                stack.append('')
            res=res[:-1]
            tmp=""
        else:#숫자
                tmp+=ch
                res+=ch
                
print(len(res))