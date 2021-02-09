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
            if '#' in trie:
                trie['#']+=1
            else:
                trie['#']=1
    def search(self, word):
        trie=self.trie
        for ch in word:
            if ch not in trie:
                return 0
            trie=trie[ch]
        return trie['#']
def solution(words, queries):
    answer = []
    word_tb=defaultdict(int)
    prefix_dict=defaultdict(Trie)
    suffix_dict=defaultdict(Trie)
    for word in words:
        prefix_dict[len(word)].addWord(word)
        suffix_dict[len(word)].addWord(word[::-1])
        word_tb[len(word)]+=1
    for query in queries:
        if query[0]==query[-1]=='?':
            answer.append(word_tb[len(query)])
        elif query[0]=='?':
            _query=query[query.rfind('?')+1:]
            answer.append(suffix_dict[len(query)].search(_query[::-1]))
        else:
            _query=query[:query.find('?')]
            answer.append(prefix_dict[len(query)].search(_query))
    return answer