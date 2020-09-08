import sys

def is_p(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

r = sys.stdin.readline
M= int(r())
N= int(r())
res = [x for x in range(M,N+1) if is_p(x)]
if not res:
    print("-1")
else:
    print(sum(res))
    print(res[0])

