import sys
r=sys.stdin.readline
S=r().strip()
stack=[]
for ch in S:
    stack.append(ch)
    if ''.join(stack[-4:])=="PPAP":
        i=3
        while i>0:
            i-=1
            stack.pop()
if len(stack)==1 and stack[0]=="P":
    print("PPAP")
else:
    print("NP")
    