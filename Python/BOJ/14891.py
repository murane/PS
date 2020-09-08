import sys
r=sys.stdin.readline
one=list(r().strip())
two=list(r().strip())
three=list(r().strip())
four=list(r().strip())
def rotate_tooth(arr:list, direction:int):
    if direction==1:#시계방향
        tmp=arr[-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=tmp
    else:#반시계방향
        tmp=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[-1]=tmp
def rotate_one(direction):
    #1번은 일단 돌아감...
    if one[2]==two[6]:
        rotate_tooth(one,direction)
    else:
        #2번이 돌아감 
        if two[2]==three[6]:
            rotate_tooth(one,direction)
            rotate_tooth(two,-direction)
        else:
            #3번도 돌아감
            if three[2]==four[6]:
                rotate_tooth(one,direction)
                rotate_tooth(two,-direction)
                rotate_tooth(three,direction)
            else:
                rotate_tooth(one,direction)
                rotate_tooth(two,-direction)
                rotate_tooth(three,direction)
                rotate_tooth(four,-direction)
def rotate_two(direction):
    #2번은 일단 돌아감
    if one[2]!=two[6]:
        #1번도 같이 돌아감
        rotate_tooth(one,-direction)
    if two[2]==three[6]:
        rotate_tooth(two,direction)
    else:
        #3번도 돌아간다.
        if three[2]==four[6]:
            rotate_tooth(two,direction)
            rotate_tooth(three,-direction)
        else:
            rotate_tooth(two,direction)
            rotate_tooth(three,-direction)
            rotate_tooth(four,direction)
def rotate_three(direction):
    if three[2]!=four[6]:
        rotate_tooth(four,-direction)
    if two[2]==three[6]:
        rotate_tooth(three,direction)
    else:
        if one[2]==two[6]:
            rotate_tooth(three,direction)
            rotate_tooth(two,-direction)
        else:
            rotate_tooth(three,direction)
            rotate_tooth(two,-direction)
            rotate_tooth(one,direction) 
def rotate_four(direction):
    if three[2]==four[6]:
        rotate_tooth(four,direction)
    else: 
        if two[2]==three[6]:
            rotate_tooth(four,direction)
            rotate_tooth(three,-direction)
        else:
            #3번도 돌아감
            if one[2]==two[6]:
                rotate_tooth(four,direction)
                rotate_tooth(three,-direction)
                rotate_tooth(two,direction)
            else:
                rotate_tooth(one,-direction)
                rotate_tooth(two,direction)
                rotate_tooth(three,-direction)
                rotate_tooth(four,direction)
def calc():
    stat=0
    if one[0]=='1':
        stat+=1
    if two[0]=='1':
        stat+=2
    if three[0]=='1':
        stat+=4
    if four[0]=='1':
        stat+=8
    return stat
for _ in range(int(r())):
    num,dire=map(int,r().split())
    #극이 같으면 가만히 있고 극이다르면 회전한 반대방향으로 회전하게됨
    if num==1:
        rotate_one(dire)
    elif num==2:
        rotate_two(dire)
    elif num==3:
        rotate_three(dire)
    elif num==4:
        rotate_four(dire)
print(calc())   
