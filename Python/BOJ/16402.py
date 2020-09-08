import sys
from collections import defaultdict
r=sys.stdin.readline
N,M=map(int,r().split())
kingdoms=[]
parents=[]
dependency=defaultdict(list)
for _ in range(N):
    kingdom=r().split()[2]
    kingdoms.append(kingdom)
    parents.append(kingdom)
for _ in range(M):
    line = r().strip()
    former = line.split(",")[0].split()[2]
    latter = line.split(",")[1].split()[2]
    winner,loser="",""
    if line.split(",")[2]=='1':#전자가 이김
        winner=former
        loser=latter
    else:#후자가 이김
        winner=latter
        loser=former
    #둘다 종주국일때
    if winner in parents and loser in parents:
        try:
            dependency[winner].extend(dependency.pop(loser)+[loser])
        except:
            dependency[winner].extend([loser])
        parents.remove(loser)
    else:
        #종주국이 다른 속국을 공격하거나 속국이 자신의 종주국을 공격하는경우
        if winner not in parents:#속국이 이김
            if winner in dependency[loser]:#반역 성공
                dependency[winner].extend(dependency.pop(loser)+[loser])
                dependency[winner].remove(winner)
                parents.remove(loser)
                parents.append(winner)
            else:#
                for kingdom in dependency.keys():
                    if winner in dependency[kingdom]:
                        dependency[kingdom].extend(dependency.pop(loser)+[loser])
                        parents.remove(loser)
                        break
        else:#종주국이 이김
            if loser in dependency[winner]:#자신의 속국을 진압
                continue
            else:
                for kingdom in dependency.keys():
                    if loser in kingdom:
                        dependency[winner].extend(dependency.pop(kingdom)+[kingdom])
                        parents.remove(kingdom)
                        break
print(len(parents))
for name in sorted(parents):
    print(f'Kingdom of {name}')
    