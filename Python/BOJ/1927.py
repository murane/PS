import sys
r=sys.stdin.readline
class Heap():
    def __init__(self):
        self.heap=[None]
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
    def push(self,n):
        self.heap.append(n)
        i=len(self.heap)-1
        while i>1 and self.heap[i//2]<self.heap[i]:
            self.swap(i,i//2)
            i=i//2
    def pop(self):
        if len(self.heap)==1:
            return 0
        self.swap(1,len(self.heap)-1)
        ret=self.heap.pop()
        self.heapify(1)
        return ret
    def heapify(self,i):
        l=i*2 if i*2 <= len(self.heap)-1 else -1
        r=i*2+1 if i*2+1 <= len(self.heap)-1 else -1
        if l==-1 and r==-1:
            return
        elif l!=-1 and r==-1:
            child=l
        else:
            child= l if self.heap[l]>self.heap[r] else r
        if self.heap[i]<self.heap[child]:
            self.swap(i,child)
            self.heapify(child)
heap=Heap()
for _ in range(int(r())):
    query=int(r())
    if query==0:
        print(heap.pop())
    else:
        heap.push(query)