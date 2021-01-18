#트리를 구성하고 설명에따라 dfs트리 dp를 사용하면된다.
import sys
r=sys.stdin.readline
N,R,Q=map(int,r().split())
#서로연결된 edge를 통해 그래프를 나타낸다
edge=[set() for _ in range(N+1)]
sys.setrecursionlimit(10**9)
for _ in range(N-1):
    a,b=map(int,r().split())
    edge[a].add(b)
    edge[b].add(a)
#n번 노드의 부모노드를 나타낸다
tree=[-1]*(N+1)
#n번 노드를 루트로하는 서브트리의 정점의 갯수를 나타낸다
dp=[0]*(N+1)
def make_tree(parent):
    #루트로부터 내려가며 루트에서부터 각 자식노드의 부모노드로의
    #간선을 제거하므로 tree가 구성된다.
    for child in edge[parent]:
        #각각의 자식노드를 tree배열에 저장하고
        tree[child]=parent
        #부모간선은 없애서 자식으로의 간선만 남긴다
        edge[child].discard(parent)
        #이를 재귀적으로 수행한다
        make_tree(child)
def dfs(node):
    #dp배열을 구성하는 함수로
    #리프노드는 1로 설정하고
    if len(edge[node])==0:
        dp[node]=1
        return dp[node]
    else:
        #재귀적으로 자식노드들의 dp값을 순회하여 저장한다.
        tmp=0
        for child in edge[node]:
            tmp+=dfs(child)
        dp[node]=tmp+1
    return dp[node]
make_tree(R)
dfs(R)
for _ in range(Q):
    print(dp[int(r())])
#최대 10만개의 노드를 트리를 구성하며 한번 순회하고
#dfs를 탐색하며 한번 순회하므로 20만?정도에 비례한다.
