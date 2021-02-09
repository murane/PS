from copy import deepcopy
def openLock(lock,M,N):
    for i in range(M-1,M+N-1):
        for j in range(M-1,M+N-1):
            if lock[i][j]!=1:
                return False
    return True
def verify(key, lock):
    M=len(key)
    N=len(lock)
    for x in range(N-M+1):
        for y in range(N-M+1):
            tb=deepcopy(lock)
            for i in range(M):
                for j in range(M):
                    tb[x+i][y+j]^=key[i][j]
            if openLock(tb,M,N-2*M+2):
                return True
    return False
def rotate90(key):
    copiedkey=[]
    for y in range(len(key)):
        tmp=[]
        for x in range(len(key)):
            tmp.append(key[x][y])
        copiedkey.append(list(reversed(tmp)))
    return copiedkey
def solution(key, lock):
    M=len(key)
    N=len(lock)
    L=N+2*M-2
    tb=[[0]*L for _ in range(L)]
    for i in range(M-1,M+N-1):
        for j in range(M-1,M+N-1):
            tb[i][j]=lock[i-(M-1)][j-(M-1)]
    if verify(key,tb):
        return True
    key_90=rotate90(key)
    if verify(key_90,tb):
        return True
    key_180=rotate90(key_90)
    if verify(key_180,tb):
        return True
    key_270=rotate90(key_180)
    if verify(key_270,tb):
        return True
    else:
        return False