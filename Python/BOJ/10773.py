import sys
r=sys.stdin.readline
stack=[]
for _ in range(int(r())):
    num=int(r())
    if num==0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))