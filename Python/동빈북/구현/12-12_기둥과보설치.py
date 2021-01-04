def solution(n, build_frame):
    answer = []
    def valid(x,y,_type):
        if _type==1:#보
            #양쪽에 기둥이 하나라도 있으면
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                return True
            #양쪽에 보가 있으면
            elif [x-1,y,1] in answer and [x+1,y,1] in answer:
                return True
            else:
                return False
        elif _type==0:#기둥
            #바닥이거나 아래에 기둥이 있으면
            if [x,y-1,0] in answer or y==0:
                return True
            else:
                #왼쪽 끝이고 아래에 보가 있음
                if x==0 and [x,y,1] in answer:
                    return True
                #오른쪽 끝이고 위래에 보가 있음
                elif x==n-1 and [x-1,y,1] in answer:
                    return True
                #가운데에 위치하고 왼쪽에만 보가 있음
                elif [x,y,1] in answer and [x-1,y,1] not in answer:
                    return True
                #가운데에 위치하고 오른쪽에만 보가 있음
                elif [x-1,y,1] in answer and [x,y,1] not in answer:
                    return True
                else:
                    return False
    for x,y,a,b in build_frame:
        if b==1:#설치
            if valid(x,y,a):
                    answer.append([x,y,a])
        #삭제
        elif b==0:
            answer.remove([x,y,a])
            if not answer: continue
            for each in answer:
                if not valid(*each):
                    answer.append([x,y,a])
                    break
    answer.sort(key=lambda x: (x[0],x[1],-x[2]))
    return answer
if __name__ == '__main__':
    n=5
    build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    solution(n,build_frame)
    