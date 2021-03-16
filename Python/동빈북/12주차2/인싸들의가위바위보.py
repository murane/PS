import sys
r=sys.stdin.readline
N,K=map(int,r().split())
info=[]
for _ in range(N):
    info.append(list(map(int,r().split())))
Ky=list(map(int,r().split()))#경희
Mi=list(map(int,r().split()))#민호

winCnt=[0,0,0]
useHand=[False]*N

def sol(player1,player2,winCnt,useHand,ky,mi):
    #print(f'{player1} {player2} {winCnt} {useHand}')
    if all([x==True for x in useHand]):
        return
    if winCnt[0]==K:
        print(1)
        exit(0)
    if winCnt[1]==K or winCnt[2]==K:
        return
    p1Hand=-1
    p2Hand=-1
    if player1==1:
        p1Hand=Ky[ky]-1
    if player1==2:
        p1Hand=Mi[mi]-1
    if player2==1:
        p2Hand=Ky[ky]-1
    if player2==2:
        p2Hand=Mi[mi]-1
    if p1Hand==-1:
        for i in range(N):
            if useHand[i]:continue
            winCntTmp=winCnt[:]
            useHandTmp=useHand[:]
            useHandTmp[i]=True
            if info[i][p2Hand]==2:
                winCntTmp[0]+=1
                if player2==1:
                    sol(0,2,winCntTmp,useHandTmp,ky+1,mi)
                if player2==2:
                    sol(0,1,winCntTmp,useHandTmp,ky,mi+1)
            else:
                winCntTmp[player2]+=1
                if player2==1:
                    sol(1,2,winCntTmp,useHandTmp,ky+1,mi)
                if player2==2:
                    sol(1,2,winCntTmp,useHandTmp,ky,mi+1)
    else:
        if info[p1Hand][p2Hand]==2:#p1이 이김
            winCnt[player1]+=1
            sol(0,player1,winCnt,useHand,ky+1,mi+1)
        else:
            winCnt[player2]+=1
            sol(0,player2,winCnt,useHand,ky+1,mi+1)

sol(0,1,winCnt,useHand,0,0)
print(0)