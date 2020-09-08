import sys
r=sys.stdin.readline

for _ in range(int(r())):
    p=r().strip()
    n=int(r())
    numbers=r()[1:-2].split(',')
    direction=True
    flg=True
    for func in p:
        if func=='R':
            direction = not direction
        else:
            if n==0:
                flg=False
                break
            else:
                if direction:
                    numbers=numbers[1:]
                else:
                    numbers=numbers[:-1]
                n-=1
    if flg:
        print('['+','.join(numbers if direction else list(reversed(numbers)))+']')
    else:
        print("error")