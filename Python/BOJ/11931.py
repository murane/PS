import sys
r=sys.stdin.readline
arr=[]
for _ in range(int(r())):
    arr.append(int(r()))
for num in sorted(arr,reverse=True):
    print(num)