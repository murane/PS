import math
from string import ascii_lowercase
from collections import Counter
def valid(str1):
    if str1[0] in ascii_lowercase and str1[1] in ascii_lowercase:
        return True
    else:
        return False
def solution(str1, str2):
    counter,second=Counter(),Counter()
    union,intersect=0,0
    for i in range(0,len(str1)-1):
        if valid(str1[i:i+2].lower()):
            counter[str1[i:i+2].lower()]+=1
    for j in range(0,len(str2)-1):
        if valid(str2[j:j+2].lower()):
            second[str2[j:j+2].lower()]+=1
    for k,v in counter.items():
        if second[k]==0:
            union+=1
        else:
            union+=max(v,second[k])
            intersect+=min(v,second[k])
    for k,v in second.items():
        if counter[k]==0:
            union+=1
    return int(math.floor(intersect/union*65536))
if __name__ == '__main__':
	print(solution("aabba","AAAA12"))
	