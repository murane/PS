import bisect
from collections import defaultdict
def solution(info, query):
    infoDict=defaultdict(list)
    for each in info:
        apply=each.split()
        a,b,c,d=apply[:4]
        stat = int(apply[4])
        infoDict[(a,b,c,d)].append(stat)
        infoDict[('-',b,c,d)].append(stat)
        infoDict[(a,'-',c,d)].append(stat)
        infoDict[(a,b,'-',d)].append(stat)
        infoDict[(a,b,c,'-')].append(stat)
        infoDict[('-','-',c,d)].append(stat)
        infoDict[(a,'-','-',d)].append(stat)
        infoDict[(a,b,'-','-')].append(stat)
        infoDict[('-',b,'-',d)].append(stat)
        infoDict[(a,'-',c,'-')].append(stat)
        infoDict[('-',b,c,'-')].append(stat)
        infoDict[('-','-','-',d)].append(stat)
        infoDict[('-',b,'-','-')].append(stat)
        infoDict[('-','-',c,'-')].append(stat)
        infoDict[(a,'-','-','-')].append(stat)
        infoDict[('-','-','-','-')].append(stat)
    for k in infoDict.keys():
        infoDict[k].sort()
    ans=[]
    for each in query:
        detail=[x for x in each.split() if x!='and']
        target=infoDict[(detail[0],detail[1],detail[2],detail[3])]
        target_stat=int(detail[4])
        idx=bisect.bisect_left(target,target_stat)
        ans.append(len(target)-idx)
    return ans

if __name__ == '__main__':
    info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    solution(info,query)
    