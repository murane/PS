from collections import deque
def ckValid(s:str):
    cur=0
    openBr=set(['(','[','{'])
    closeBr=set([')',']','}'])
    pair={'(':')','[':']','{':'}'}
    stack=[]
    for br in s:
        if br in openBr:
            cur+=1
            stack.append(br)
        else:
            #열린적없는짝을 닫음
            if not stack:return False
            before=stack.pop()
            #짝이 안맞음
            if pair[before]!=br:return False
            cur-=1
    #열린게 다 안닫힘
    if cur!=0: return False
    return True
def solution(s):
    answer = 0
    q=deque(s)
    for i in range(len(s)):
        if ckValid(list(q)):
            answer+=1
        q.rotate(1)
    return answer
if __name__ == '__main__':
    solution("[](){}")
    