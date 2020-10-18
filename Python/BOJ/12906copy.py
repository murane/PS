#예제는 잘 나오는데 메모리초과.. 더 효율적으로 짜기 위한 생각을 해야겠습니다
from collections import deque

def ck(A, B, C):
    if set(A) != set('A') and A: return False
    if set(B) != set('B') and B: return False
    if set(C) != set('C') and C: return False
    return True

def sol():
    q = deque()
    q.append([S1, S2, S3, 0])
    visit = set()
    visit.add(S1+'/'+S2+'/'+S3)
    while q:
        A, B, C, result = q.popleft()
        if ck(A, B, C):
            return result
        if A:
            last = A[-1]
            tempA = A[:len(A)-1]
            tempB = B + last
            if tempA+'/'+tempB+'/'+C not in visit:
                visit.add(tempA+'/'+tempB+'/'+C)
                q.append([tempA, tempB, C, result+1])
            tempC = C + last
            if tempA+'/'+B+'/'+tempC not in visit:
                visit.add(tempA+'/'+B+'/'+tempC)
                q.append([tempA, B, tempC, result+1])
        if B:
            last = B[-1]
            tempB = B[:len(B)-1]
            tempA = A + last
            if tempA+'/'+tempB+'/'+C not in visit:
                visit.add(tempA+'/'+tempB+'/'+C)
                q.append([tempA, tempB, C, result+1])
            tempC = C + last
            if A+'/'+tempB+'/'+tempC not in visit:
                visit.add(A+'/'+tempB+'/'+tempC)
                q.append([A, tempB, tempC, result+1])
        if C:
            last = C[-1]
            tempC = C[:len(C)-1]
            tempA = A + last
            if tempA+'/'+B+'/'+tempC not in visit:
                visit.add(tempA+'/'+B+'/'+tempC)
                q.append([tempA, B, tempC, result+1])
            tempB = B + last
            if A+'/'+tempB+'/'+tempC not in visit:
                visit.add(A+'/'+tempB+'/'+tempC)
                q.append([A, tempB, tempC, result+1])

S1, S2, S3 = '', '', ''
a = input()
if len(a) != 1:
    a = a.split(' ')
    S1 += a[1]
b = input()
if len(b) != 1:
    b = b.split(' ')
    S2 += b[1]
c = input()
if len(c) != 1:
    c = c.split(' ')
    S3 += c[1]
print(sol())