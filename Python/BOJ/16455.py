import random
def kth(a:list,k:int):
    def partition(lst,start,end):
    def qselect(lst,start,end,k):
        if start==end:
            return lst[start]
        while True:
            pos=partition(lst,start,end)
            bound=(len(a)*3)//4
            if pos-start>bound or end-pivPos>bound:
                continue
            pos=pivPos
            if cur==k:
                return lst[pos]
            elif pos<k:
                return qselect(lst,pos+1,end,k)
            else:
                return qselect(lst,start,pos-1,k)
    return qselect(a,0,len(a)-1,k)
if __name__ == '__main__':
    res=kth([3, 2, 5, 1, 7, 9, 6, 4, 8, 10],5)
    print(res)
if __name__ == '__main__':
    res=kth([3, 2, 5, 1, 7, 9, 6, 4, 8, 10],5)
    print(res)
   