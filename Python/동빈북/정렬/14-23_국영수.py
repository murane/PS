import sys
r=sys.stdin.readline
stdents=[]
for _ in range(int(r())):
    name,a,b,c=r().split()
    stdents.append([name,int(a),int(b),int(c)])
#조건에맞게 정렬
stdents.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for each in stdents:
    print(each[0])