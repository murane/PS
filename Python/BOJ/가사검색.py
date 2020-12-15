from collections import defaultdict
def is_match(pattern,word):
    if pattern.startswith('?'):
        for i in range(pattern.rfind('?')+1,len(word)):
            if pattern[i]!=word[i]:
                return False
        return True
    else:
        for i in range(pattern.find('?')):
            if pattern[i]!=word[i]:
                return False
        return True
def solution(words, queries):
    answer = []
    res_tb=dict()
    word_tb=defaultdict(list)
    for word in words:
        word_tb[len(word)].append(word)
    for query in queries:
        if query in res_tb:
            answer.append(res_tb[query])
            continue
        tmp=0
        for word in word_tb[len(query)]:
            if is_match(query,word):
                tmp+=1
        res_tb[query]=tmp
        answer.append(tmp)
    return answer

if __name__ == '__main__':
    words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries=["fro??", "????o", "fr???", "fro???", "pro?"]
    solution(words,queries)

    