import sys

def binSearch(arr, N):
    hi,lo=len(arr)-1,0
    while lo<=hi:
        mid = (hi+lo)//2
        if arr[mid]==N:
            return True
        elif arr[mid] < N:
            lo=mid + 1
        else:
            hi=mid - 1
    return False


r=sys.stdin.readline

N=int(r())
N_list=list(map(int,r().split()))
M=int(r())
M_list=list(map(int,r().split()))
N_list=sorted(N_list)
for num in M_list:
    if binSearch(N_list,num):
        print("1")
    else:
        print("0")
