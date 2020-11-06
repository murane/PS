from collections import Counter
def solution(a):
    counter=Counter(a)
    if len(a)==1:
        return 0
    elif len(a)==2:
        return 1
    else:
        if counter.most_common()[1]==1:
            return 2
        ans=0
        for num,cnt in counter.most_common():
            cur=0
            tmp=0
            while True:
                cur=getNext(a,num,cnt,cur,len(a))
                if cur!=-1:tmp+=2
                if cur==-1 or cur>=len(a)-1:
                    ans=max(tmp,ans)
                    break
        return ans
                
def getNext(a,num,cnt,cur,limit):
    if a[cur]==num:
        cur+=1
        if cur==len(a)-1:
            return -1
        while a[cur]==num:
            if cur==len(a)-1:
                return -1
            cur+=1
        return cur+1
    else:
        cur+=1
        if cur==len(a)-1:
            return -1
        while a[cur]!=num:
            if cur==len(a)-1:
                return -1
            cur+=1
        return cur+1
            

if __name__ == '__main__':
    a=[0,3,3,0,7,2,0,2,2,0]
    print(solution(a))
    #print(solution(info, query))
	