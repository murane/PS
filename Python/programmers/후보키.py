from itertools import combinations
def check(relation,keys)->bool:
    res=set()
    for tup in relation:
        tmp=[tup[x] for x in keys]
        res.add(tuple(tmp))
    if len(res)==len(relation):
        print(*keys)
        return True
    else: return False
def solution(relation):
    leng=len(relation[0])    #릴레이션의 튜플 총 갯수
    candi=[]                #후보키가 될수 있는 그룹 리스트
    for i in range(1,leng+1):             #1~length까지 모든 길이의 후보키 군을 검사
        for keys in combinations(list(range(leng)),i):
            keys=list(keys)
            flg=True
            for each_candi in candi:        #단 최소성을 위해 이미 후보군에 올라온 것은 제외한다
                if set(each_candi).issubset(set(keys)): flg=False
            if not flg: continue
            if check(relation,keys): candi.append(keys)
    return len(candi)
if __name__ == '__main__':
    relation=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    solution(relation)