from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        counter=Counter()
        for order in orders:
            for tup in combinations(order,i):
                counter[tuple(sorted(tup))]+=1
        tmp=[]
        for k,v in counter.most_common():
            if not tmp and v>1:
                tmp.append((k,v))
            elif tmp:
                if v==tmp[-1][1] and v>1:
                    tmp.append((k,v))
                else:
                    break
        answer.extend([''.join(sorted(x[0])) for x in tmp])
    answer.sort()
    return answer