def check_valid(s):
    if s=='': return True
    stack=[]
    while s:
        cur=s[0]
        s=s[1:]
        if cur=='(':
            stack.append(cur)
        else:
            if not stack: return False
            else: stack.pop()
    return True
def check_balance(s):
    if s=='': return True
    o,c=0,0
    for ch in s:
        if ch=='(':o+=1
        if ch==')':c+=1
    return True if o==c else False
def rev(s):
    tmp=""
    for ch in s[1:-1]:
        if ch=='(':
            tmp+=')'
        elif ch==')':
            tmp+='('
    return tmp
def solution(p):
    answer = ''
    while p:
        u=p[0]
        p=p[1:]
        while not check_balance(u):
            u+=p[0]
            p=p[1:]
        if check_valid(u):
            answer+=u
        else:
            answer+=('('+solution(p)+')'+rev(u))
            break
    return answer
if __name__ == '__main__':
    p="()))((()"
    solution(p)
    