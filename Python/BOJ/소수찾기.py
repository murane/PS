from itertools import permutations
def is_p(num):
    if num==1 or num==0:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
        
    
def solution(numbers):
    answer = 0
    tmp = []
    for i in range(1,len(numbers)+1):
        for numstr in permutations(numbers, i):
            tmp.append(int(''.join(numstr)))
    
    tmp = list(set(tmp))
    for num in tmp:
        if is_p(num):
            answer+=1
    return answer
a=set([x for x in range(2,100)])
for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
print(len(a))


