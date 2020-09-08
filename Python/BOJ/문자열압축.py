def solution(s):
    answer = 0
    length=[]
    tmp=0
    for i in range(1,len(s)//2+1):
        tmpstr=s
        curstr=''
        cnt=1
        tmpLength=0
        while tmpstr:
            #처음경우 갱신
            if curstr=='':
                curstr=tmpstr[:i]
            else:
                if curstr==tmpstr[:i]:
                    cnt+=1
                else:
                    if cnt==1:
                        tmpLength+=(len(curstr))
                    else:
                        tmpLength+=(len(curstr)+len(str(cnt)))
                    curstr=tmpstr[:i]
                    cnt=1
            tmpstr=tmpstr[i:]
            if not tmpstr:
                if cnt==1:
                        tmpLength+=(len(curstr))
                else:
                    tmpLength+=(len(curstr)+len(str(cnt)))
        length.append(tmpLength)
    
    return min(length)
if __name__ == "__main__":
    s = "a"
    print(solution(s))    