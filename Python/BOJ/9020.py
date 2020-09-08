import sys
r = sys.stdin.readline
prime=[0,0]+[1]*(10000-1)
for num in range(2, 10000+1):
    if prime[num]==1:
        for j in range(num*2, len(prime), num):
            prime[j]=0
for _ in range(int(r())):
    n=int(r())
    candidates=[]
    answer=0
    for i in range(n//2,n):
        if prime[i] and prime[n-i]:
            answer=i
            break
    print(f'{n-answer} {answer}')