#괄호 열림과 닫힘을 카운트하여 균형잡힌지 확인
def isValance(s:str):
    if s=='':
        return True
    if s.count('(')==s.count(')'):
        return True
    else:
        return False

def isValid(s:str):
    if s=='':
        return True
    cur=0
    for par in s:
        if par=='(':
            cur+=1
        elif par==')':
            cur-=1
        #)가 선행하면 음수이므로 올바르지 않음
        if cur<0: return False
    return cur==0
def solution(p):
    if p=='':return ''
    u,v='',''
    #2개씩 끊어서 u,v로 나눔
    for i in range(1,len(p)//2+1):
        u,v=p[:i*2],p[i*2:]
        if isValance(u):break
    if isValid(u):
        return u+solution(v)
    else:
        u=u[1:-1]
        w=''
        for par in u:
            if par=='(':
                w+=')'
            else:
                w+='('
        return '('+solution(v)+')'+w
