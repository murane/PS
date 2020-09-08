import sys,math
r=sys.stdin.readlines
N=1000000
def primes(n):
    tb=[False,False]+[True]*n
    for i in range(2,math.ceil(n**0.5)):
        if tb[i]:
            for j in range(i*2,n,i):
                tb[j]=False
        else:
            continue
    return [x for x in range(3,n) if tb[x]]
p=primes(N)
for num in r()[:-1]:
    flg=True
    for k in range(len(p)):
        if int(num)-p[k] in p:
            flg=False
            print(f'{int(num)} = {p[k]} + {int(num)-p[k]}')
            break
    if flg:
        print( "Goldbach's conjecture is wrong.")
