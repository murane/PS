def solution(s):
    answer = []
    tmp=set()
    s=s[2:-2]
    lst=s.split("},{")
    tuples=[]
    for each in lst:
        tuples.append(list(map(int,each.split(","))))
    for tup in sorted(tuples,key=lambda x:len(x)):
        if not tmp:
            answer.append(tup[0])
        else:
            elem=list(set(tup)-tmp)[0]
            answer.append(elem)
        tmp.update(tup)
    return answer

if __name__ == '__main__':
    s="{{2},{2,1},{2,1,3},{2,1,3,4}}"
    solution(s)
    