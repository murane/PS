import sys
from collections import Counter
r=sys.stdin.readline

tb=[True]*(10**5+2)
primes=[]
for i in range(2,10**5+1):
    if tb[i]:
        primes.append(i)
        for j in range(i*2,10**5+1,i):
            tb[j]=False
def get_divisors(num):
    lst=[]
    for prime in primes:
        if num==1:break
        while num>=0 and num%prime==0:
            lst.append(prime)
            num=num//prime
    return lst
for _ in range(int(r())):
    n=int(r())
    if n<=10**5 and tb[i]:
        print(1)
        print(n)
    else:
        lst=get_divisors(n)
        if lst:
            counter=Counter(lst)
            mst=counter.most_common(1)[0]
        if not lst or mst[1]==1:
            print(1)
            print(n)
        else:
            print(mst[1])
            left=n//(mst[0]**(mst[1]-1))
            res=[mst[0]]*(mst[1]-1)+[left]
            print(*res)

