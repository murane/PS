import sys,math
r=sys.stdin.readline
def get_prime(N: int) -> list:
    tb=[False, False]+[True]*N
    size=math.ceil(N**0.5)
    for i in range(2,N):
        if tb[i]:
            for j in range(i*i,N,i):
                tb[j]=False
    return [x for x in range(N) if tb[x] and is_palindrome(x)]
def is_palindrome(num: int) -> bool:
    if str(num)==str(num)[::-1]:
        return True
    else:
        return False
    
N=int(r())
for num in get_prime(1500000):
    if num >= N:
        print(num)
        break