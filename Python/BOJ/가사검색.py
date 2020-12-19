from collections import defaultdict
class Trie():
    def __init__(self):
        self.trie=dict()
    def addWord(self, word):
        trie=self.trie
        for ch in word:
            if ch not in trie:
                trie[ch]={}
            trie=trie[ch]
            if len(word) in trie:
                trie[len(word)]+=1
            else:
                trie[len(word)]=1
    def search(self, word,length):
        trie=self.trie
        for ch in word:
            if ch not in trie:
                return 0
            trie=trie[ch]
        return trie[length]
def solution(words, queries):
    answer = []
    word_tb=defaultdict(int)
    trie,r_trie=Trie(),Trie()
    for word in words:
        trie.addWord(word)
        r_trie.addWord(word[::-1])
        word_tb[len(word)]+=1
    for query in queries:
        if query[0]==query[-1]=='?':
            answer.append(word_tb[len(query)])
        elif query[0]=='?':
            _query=query[query.rfind('?')+1:]
            answer.append(r_trie.search(_query[::-1],len(query)))
        else:
            _query=query[:query.find('?')]
            answer.append(trie.search(_query,len(query)))
    return answer

if __name__ == '__main__':
    words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries=["?????","????t"]
    solution(words,queries)

    