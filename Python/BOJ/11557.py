import sys
r=sys.stdin.readline
for _ in range(int(r())):
    most=[("dum",0)]
    for _ in range(int(r())):
        line=r().strip().split()
        if int(line[1])>most[0][1]:
            most[0]=(line[0],int(line[1]))
    print(most[0][0])