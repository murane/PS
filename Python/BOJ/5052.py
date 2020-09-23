import sys
r=sys.stdin.readline
for _ in range(int(r())):
    phoneNums=set()
    n=int(r())
    flg=True
    for _ in range(n):
        phoneNums.add(r().strip())
    for num in phoneNums:
        for i in range(len(num)-1):
            if num[:i+1] in phoneNums:
                print("NO")
                flg=False
                break
        if not flg:
            break
    if flg:
        print("YES")