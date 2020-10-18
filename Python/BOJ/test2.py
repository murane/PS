def divCon(arr,leng):
    zero,one=0,0
    #leng이 1이면 사각형의 0,1의 갯수와 arr을 반환
    if leng==2:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]==0: zero+=1
                else: one+=1
    else:
        for x,y in [(0,0),(leng//2,0),(0,leng//2),(leng//2,leng//2)]:
            tmp_0,tmp_1=0,0
            tmpArr=[]
            for j in range(x,x+leng//2):
                tmpRow=[]
                for k in range(y,y+leng//2):
                    tmpRow.append(arr[j][k])
                    if arr[j][k]==0: tmp_0+=1
                    else: tmp_1+=1
                tmpArr.append(tmpRow)
            if tmp_0==0: one+=1
            elif tmp_1==0: zero+=1
            else:
                res=divCon(tmpArr,leng//2)
                zero+=res[1]
                one+=res[2]
    return arr,zero,one

def solution(arr):
    L=len(arr)
    _,zero,one = divCon(arr,L)
    return [zero,one]
if __name__ == '__main__':
    arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
    print(solution(arr))
    #print(solution(info, query))
	