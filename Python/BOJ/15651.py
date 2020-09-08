import sys
def comb(arr, r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in comb(arr,r-1):
                yield[arr[i]] + next

def dup_comb(arr, r):
    arr= sorted(arr)
    res = []
    def gen(picked):
        if len(picked) == r:
            res.append(list(picked))
            return
        else:
            for i in range(len(arr)):
                picked.append(arr[i])
                gen(picked)
                picked.pop()
    gen([])
    return res


r=sys.stdin.readline
N,M = list(map(int,r().split()))
for part in list(comb(range(1,N+1),M)):
    for item in part:
        print(item,end=" ")
    print("")
