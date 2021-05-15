import sys
r=sys.stdin.readline
N=int(r())
arr=[]
for _ in range(N):
    arr.append(list(r().strip()))

def quad(i,j,size):
    if size==1:
        tmp=[]
        tmp.extend([arr[i][j],arr[i][j+1],arr[i+1][j],arr[i+1][j+1]])
        if not '1' in tmp:
            return '0'
        elif not '0' in tmp:
            return '1'
        else:
            return '('+''.join(tmp)+')'
    else:
        res=[]
        res.append(quad(i,j,size//2))
        res.append(quad(i,j+size,size//2))
        res.append(quad(i+size,j,size//2))
        res.append(quad(i+size,j+size,size//2))
        if all(map(lambda x:x=='0',res)):
            return '0'
        elif all(map(lambda x:x=='1',res)):
            return '1'
        else:
            return '('+''.join(res)+')'
if N==1 and arr[0][0]==1:
    print(1)
elif N==1 and arr[0][0]==0:
    print(0)
else:
    print(quad(0,0,N//2))