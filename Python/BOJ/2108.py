import sys
r=sys.stdin.readline
N=int(r())
nums=[]
mstfre=[]
tb=[0]*8001
for _ in range(N):
    v=int(r())
    tb[v+4000]+=1
    nums.append(v)
print(round(sum(nums)/N))
nums=sorted(nums)
print(nums[len(nums)//2])
fre = max(tb)
for i in range(0,8001):
    if tb[i]==fre:
        mstfre.append(i)
if len(mstfre)>1:
    print(mstfre[1]-4000)
else:
    print(mstfre[0]-4000)

print(nums[-1]-nums[0])
