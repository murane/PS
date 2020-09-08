import sys
r=sys.stdin.readline
users={}
for _ in range(int(r())):
    age,name=list(r().split())
    try:
        users[int(age)]
    except KeyError:
        users[int(age)]=[name]
    else:
        users[int(age)].append(name)
for key in sorted(list(users.keys())):
    for item in users[key]:
        print(f'{key} {item}')