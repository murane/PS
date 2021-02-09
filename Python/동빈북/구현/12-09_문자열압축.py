def solution(s):
    answer = []
    #한글자 예외처리
    if len(s)==1:
        return 1
    #길이 1 ~ 반절까지
    for i in range(1,len(s)//2+1):
        S=s
        tmp=[]
        res=""
        #tmp에 i길이 만큼씩 자른 문자열을 저장
        while True:
            if not S:break
            if len(S)<i:
                break
            else:
                cur,S=S[:i],S[i:]
                #직전문자열을 확인하여 카운트를 올린다
                if not tmp or tmp[-1][0]!=cur:
                    tmp.append([cur,1])
                elif tmp[-1][0]==cur:
                    tmp[-1][1]+=1
        #카운트수를 앞에 붙여준다
        for string,cnt in tmp:
            if cnt==1:
                res+=string
            else:
                res+=(str(cnt)+string)
        answer.append(res+S)
    return min([len(x) for x in answer])

if __name__ == '__main__':
    res=solution("a")
    print(res)

#1~ n/2까지 n길이의 문자열을 순회하므로
#n^2의 시간복잡도를 가진다
    