import sys
from collections import Counter
from string import ascii_lowercase,digits
def calcWeight(s):#입력된 36진수의 자릿수별로 가중치 카운트
    for i,ch in enumerate(reversed(s)):
        counter[ch]+=((36**i)*_36to10(ch,0))
def _36to10(a:str,idx):#36진수를 10진수로
    if len(a)<=idx: return 0
    if a[idx] in digits:
        cur=int(a[idx])
    else:
        cur=ord(a[idx])-ord("A")+10
    return cur
def _10to36(num:int):#10진수를 36진수로
    up=False
    if 0<=num<10:
        res=str(num)
    elif 10<=num<36:
        res=chr(num-10+ord("A"))
    else:
        up=True
        res=chr(num-10+ord("A")-36)
    return res,up
def Add_36_jin(a:str,b:str):
    a=a[::-1]
    b=b[::-1]
    res=""
    idx=0
    up=False
    while True:
        if len(a)<=idx and len(b)<=idx:
            if up: res+="1"
            break
        curA=_36to10(a,idx)
        curB=_36to10(b,idx)
        curAB=curA+curB
        if up:
            curAB+=1
            up=False
        tmp,up=_10to36(curAB)
        res+=tmp
        idx+=1
    return res[::-1]
            

if __name__ == '__main__':
    print(Add_36_jin("W","G"))