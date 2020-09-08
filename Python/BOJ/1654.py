import sys
from collections import Counter
r=sys.stdin.readline
read = sys.stdin.read
K,N=list(map(int,r().split()))
lens=Counter(list(read().split()))
def calc(line,length):
    tmpSum=0
    for string in line:
        tmpSum+=(int(string)//length)
    return tmpSum

def bise(length):
    while calc(lens,length)<N:
        length=length//2
    while calc(lens,length)>=N:
        length+=1
    return length-1

print(bise(int(max(lens))))