import sys
r=sys.stdin.readline
arr = [0]*10001
for _ in range(int(r())):
    arr[int(r())]+=1
for i in range(1,len(arr)):
    arr[i]+=arr[i-1]
res = [0]*len(arr)

for i in range(len(arr)):
    if arr[i]>=1:
        print(i+1)
        arr[i]-=1