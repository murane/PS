import sys
from collections import defaultdict
r=sys.stdin.readline
class Node(object):
    parent=None
    def __init__(self,num,left=-1,right=-1):
        self.num=num
        self.left=left
        self.right=right
    def is_root(self):
        if self.parent==None:
            return True
        else:
            return False
    def set_child(self,left,right):
        self.left=left
        self.right=right
    def set_parent(self,parent):
        self.parent=parent
    def get_left(self):
        if self.left==-1:
            return False
        else:
            return self.left
    def get_right(self):
        if self.right==-1:
            return False
        else:
            return self.right
N=int(r())
Tree=[None]+[Node(x) for x in range(1,N+1)] #노드 접근 인덱스를 맞추기 위해 None추가
for _ in range(N):
    num,left,right=map(int,r().split())
    Tree[num].set_child(left,right)         #노드를 미리 자식없이 생성했기 때문에
    if left!=-1:                            #메소드를 통해 추가해줍니다.
        Tree[left].set_parent(num)
    if right!=-1:
        Tree[right].set_parent(num)
root=0
width=[None]
for i in range(1,N+1):#트리 전체를 순회하며 루트노드를 찾아 저장합니다.
    if Tree[i].is_root():
        root=i
        break
def traverse(nodenum):#중위순회를 통해 왼쪽부터 접근할수 있기 때문에
    left=Tree[nodenum].get_left()#너비 리스트를 작성합니다.
    right=Tree[nodenum].get_right()
    if left:
        traverse(left)
    width.append(nodenum)
    if right:
        traverse(right)
def get_level(node):
    level=1#이진트리로 작성되있기때문에 부모를 되짚어
    if Tree[node].is_root():#log시간에 부모를 찾아냅니다.
        return level
    else:
        par=Tree[node].parent
        while par!=None:
            par=Tree[par].parent
            level+=1
    return level
traverse(root)
res=defaultdict(list)
for i in range(1,N+1):
    level=get_level(i)#레벨별 너비를 계산하기위해 해당 레벨의 모든 너비를
    res[level].append(width.index(i))#딕셔너리에 추가합니다.
ans=(0,0)
for i in range(1,len(res.keys())+1):#딕셔너리의 레벨별로 순회하여
    tmp=(0,0)                       #최대,최소값을 구하고 
    if len(res[i])==0:              #ans에 추가합니다.
        tmp=(i,1)
    else:
        tmp=(i,max(res[i])-min(res[i])+1)
    if ans[1]<tmp[1]:
        ans=tmp
print(*ans)