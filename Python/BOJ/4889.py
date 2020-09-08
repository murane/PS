import sys
def delWord(word:str,part:str)->str:
    while word.find(part)!=-1:
        word=word[:word.find(part)]+word[word.find(part)+len(part):]
    return word
r=sys.stdin.readline
cnt=0
while True:
    case=r().strip()
    cnt+=1
    if case.find('-')!=-1:
        break
    case=delWord(case,"{}")
    res=0
    res+=case.count("{{")
    case=delWord(case,"{{")
    res+=case.count("}}")
    case=delWord(case,"}}")
    res+=case.count("}{")*2
    print(f'{cnt}. {res}')