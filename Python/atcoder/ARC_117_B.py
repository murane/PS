#-*-coding:utf-9-*-
import sys
r=sys.stdin.readline
N=int(r())
arr=list(map(int,r().split()))
MOD=10**9+7
#N개의 빌딩이 있다. 
#N은 10만
arr.sort()
#일단 정렬하고...