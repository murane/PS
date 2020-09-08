import sys
r=sys.stdin.readline
S=set()
for _ in range(int(r())):
    op=r().split()
    if op[0]=='add':
        if not S.__contains__(int(op[1])):
            S.add(int(op[1]))
        else:
            continue
    elif op[0]=='remove':
        if S.__contains__(int(op[1])):
            S.remove(int(op[1]))
        else:
            continue
    elif op[0]=='check':
        if S.__contains__(int(op[1])):
            print(1)
        else:
            print(0)
    elif op[0]=='toggle':
        if S.__contains__(int(op[1])):
            S.remove(int(op[1]))
        else:
            S.add(int(op[1]))
    elif op[0]=='all':
        S.update(range(1,21))
    elif op[0]=='empty':
        S=set()
