import sys
r=sys.stdin.readline
N=int(r())
cost=list(map(int,r().split()))
money=int(r())
#가장 앞은 0이 아닌 숫자중 가장 싼 숫자
#그 외에는 가장 싼걸로
#맨앞은 0을 제외한 더 큰수로 바꾸자
#그 다음부터는 순서대로


