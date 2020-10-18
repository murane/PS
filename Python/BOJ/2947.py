import sys
r=sys.stdin.readline
arr=list(map(int,r().split()))

def p(arr):
    print(' '.join(map(str,arr)))

while True:
    if arr[0]>arr[1]:
        arr[0],arr[1]=arr[1],arr[0]
        p(arr)
    if arr[1]>arr[2]:
        arr[1],arr[2]=arr[2],arr[1]
        p(arr)
    if arr[2]>arr[3]:
        arr[2],arr[3]=arr[3],arr[2]
        p(arr)
    if arr[3]>arr[4]:
        arr[3],arr[4]=arr[4],arr[3]
        p(arr)
    if arr==[1,2,3,4,5]:
        break