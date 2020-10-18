def solution(s):
    if len(s) == s.count(s[0]):
        return 0
    else:
        words = []
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                words.append(s[i:j+1])
        