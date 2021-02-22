import sys
def test(lst):
    tmp=[]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j: continue
            tmp.append(lst[i]*2-lst[j])
    return sorted(list(set(tmp+lst)))


