import sys
r=sys.stdin.readline
for _ in range(int(r())):
    ps=r().strip()
    stack=[]
    if len(ps)%2==1:
        print("NO")
    else:
        flg=True
        for ch in ps:
            if ch=='(':
                stack.append(ch)
            elif ch==')':
                try:
                    stack.pop()
                except Exception as e:
                    flg=False

        if flg==False or len(stack)!=0:
            print("NO")
        else:
            print("YES")