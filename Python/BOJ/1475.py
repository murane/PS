import sys,math
r=sys.stdin.readline
N=r().strip()
arr=[0]*9
for num in N:
    if int(num)==9:
        arr[6]+=1
    else:
        arr[int(num)]+=1
arr[6]=math.ceil(arr[6]/2)
print(int(max(arr)))