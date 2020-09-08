import sys
r=sys.stdin.readline
N,M=map(int,r().split())
pocketmon_dict={}
pocketmon_list=[""]
for i in range(N):
    tmp=r().strip()
    pocketmon_dict[tmp]=i+1
    pocketmon_list.append(tmp)
for _ in range(M):
    command=r().strip()
    if command.isdigit():
        print(pocketmon_list[int(command)])
    else:
        print(pocketmon_dict[command])
