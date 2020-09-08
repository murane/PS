class tree():
    Nodes={}
    NodesToDel=[]
    def __init__(self, Nodes):
        for i in range(N):
            self.Nodes[i]=Nodes[i]
    def countLeaf(self):
        NodeSet=set([k for k in self.Nodes.keys()])
        parentSet=set([v for v in self.Nodes.values() if v!=-1])
        return len(NodeSet-parentSet)
    def deleteNode(self,n):
        for k,v in self.Nodes.items():
            if v==n:
                self.deleteNode(k)
        self.NodesToDel.append(n)
    def execute(self):
        for node in self.NodesToDel:
            del self.Nodes[node]
import sys
r=sys.stdin.readline
N=int(r())
Nodes=list(map(int,r().split()))
NodeToDel=int(r())
#key->노드번호, value->부모노드
#i->노드번호, Nodes[i]->부모노드
Tree = tree(Nodes)
Tree.deleteNode(NodeToDel)
Tree.execute()
print(Tree.countLeaf())
