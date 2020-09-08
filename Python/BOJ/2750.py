import sys
r=sys.stdin.readline
res=[]
for _ in range(int(r())):
    res.append(int(r()))

for i in range(len(res)-1):
    for j in range(len(res)-1):
        if res[j]>res[j+1]:
            res[j],res[j+1]=res[j+1],res[j]
for num in res:
    print(num)