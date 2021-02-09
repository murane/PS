import sys
import bisect
r=sys.stdin.readline
arr=list(map(int,r().split()))
def selection_sort(arr):
    for i in range(len(arr)-1):
        minimum=i
        for j in range(i+1,len(arr)):
            if arr[minimum]>arr[j]:
                minimum=j
        arr[minimum],arr[i]=arr[i],arr[minimum]
def insert_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    piv=arr[0]
    lst=arr[1:]
    l=[x for x in lst if x<=piv]
    r=[x for x in lst if x>piv]
    return quick_sort(l)+[piv]+quick_sort(r)
# selection_sort(arr)
# insert_sort(arr)
quick_sort(arr)
print(*quick_sort(arr))