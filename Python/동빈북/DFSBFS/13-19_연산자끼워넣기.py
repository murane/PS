import sys
r=sys.stdin.readline
N=int(r())
numbers=list(map(int,r().split()))
plus,minus,mul,div=map(int,r().split())
lst=[]
#dfs로 모든 연산의 경우를 탐색할 수 있다.
def calc(curNum,curIdx,plus,minus,mul,div):
    if curIdx==len(numbers):
        lst.append(curNum)
        return
    if plus>0:
        calc(curNum+numbers[curIdx],curIdx+1,plus-1,minus,mul,div)
    if minus>0:
        calc(curNum-numbers[curIdx],curIdx+1,plus,minus-1,mul,div)
    if mul>0:
        calc(curNum*numbers[curIdx],curIdx+1,plus,minus,mul-1,div)
    if div>0:
        if curNum<0:
            calc(-(-curNum//numbers[curIdx]),curIdx+1,plus,minus,mul,div-1)
        else:
            calc(curNum//numbers[curIdx],curIdx+1,plus,minus,mul,div-1)

calc(numbers[0],1,plus,minus,mul,div)
print(max(lst))
print(min(lst))

#4가지 연산에 대해 최대 10번 까지 깊이가 구성되므로
#대략 2^20승이 최악의 경우의 수로 예상된다
#재귀함수로 인한 메모리부하에 대해서는 잘 모르겠다.