import sys
r=sys.stdin.readline
N,L=map(int,r().split())
floor=[]
for _ in range(N):
    leng,direction=map(int,r().split())
    floor.append((leng,direction))

def can_elevalate(f):
    if f==N:
        return False
    cur_floor_pos,cur_leng = get_cur_pos(time,f)
    next_floor_pos,nxt_leng = get_cur_pos(time,f+1)

    if cur_floor_pos>next_floor_pos:
        l,l_len=next_floor_pos,nxt_leng
        r,r_len=cur_floor_pos,cur_leng
    else:
        l,l_len=cur_floor_pos,cur_leng
        r,r_len=next_floor_pos,nxt_leng
    if l+l_len<r:
        return False
    return True

def get_cur_pos(time,f):
    leng,di=floor[f-1]
    cycle=L-leng
    if cycle==0:
        return 0,leng
    q,r=divmod(time,cycle)
    #짝수면 원래방향
    if q%2==0:
        if di==1:
            return cycle-r,leng
        else:
            return r,leng
    #홀수면 반대방향
    else:
        if di==1:
            return r,leng
        else:
            return cycle-r,leng
time=0
current_floor=1
while current_floor<N:
    time+=1
    while can_elevalate(current_floor):
        current_floor+=1
print(time)