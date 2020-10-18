import sys
r=sys.stdin.readline
N=int(r())
x=list(map(int,r().split()))
arrSum=[]
arrSquareSum=[]
for num in x:
    arrSum.append(abs(num))
    arrSquareSum.append(abs(num**2))
print(sum(arrSum))
print(format(sum(arrSquareSum)**0.5,'.15f'))
print(max(arrSum))

