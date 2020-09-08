import sys
r=sys.stdin.readline
stack=[]
for _ in range(int(r())):
    op=r().split()
    if op[0]=='push':
        stack.append(op[1])
    elif op[0]=='pop':
        if len(stack)==0:
            print("-1")
        else:
            print(stack.pop())
    elif op[0]=='size':
        print(len(stack))
    elif op[0]=='empty':
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif op[0]=="top":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[-1])