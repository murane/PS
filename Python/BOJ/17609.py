import sys
r=sys.stdin.readline
def pal(s):
    left,right=0,len(s)-1
    ret=0
    while left<=right and ret==0:
        if s[left]==s[right]:#회문인 경우
            left,right=left+1,right-1
        else:           #유사회문을 확인해보자..
            l,r=left+1,right
            while l<=r:
                if s[l]!=s[r]:
                    ret+=1
                    break
                l,r=l+1,r-1
            l,r=left,right-1
            while l<=r:
                if s[l]!=s[r]:
                    ret+=1
                    break
                l,r=l+1,r-1
            return ret
    return ret

for _ in range(int(r())):
    print(pal(r().strip()))
