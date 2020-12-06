import re
from operator import itemgetter
from collections import defaultdict
def solution(word, pages):
    tb=dict()
    default_stat=dict()
    link_stat=defaultdict(list)
    matching_stat=defaultdict(int)
    word=word.lower()
    for i in range(len(pages)):
        pages[i]=pages[i].lower()
    for i,page in enumerate(pages):
        tmp=re.search(r'<meta .* content=\"(.*)\".*/>', page)
        url=tmp.group(1)
        tb[url]=i
        tb[i]=url
        cnt=len(re.findall(r'[^a-z]+('+word+')[^a-z]+',page))
        default_stat[i]=cnt
        links=re.findall(r'<a.*href=\"(.*)\".*>',page)
        link_stat[i].extend(links)
    for i in range(len(pages)):
        for link in link_stat[i]:
            if link in tb:
                matching_stat[tb[link]]+=(default_stat[i]/len(link_stat[i]))
        matching_stat[i]+=default_stat[i]
    res = list(matching_stat.items())
    res.sort(key=itemgetter(1,0),reverse=True)
    return res[0][0]

if __name__ == '__main__':
    word="Muzi"
    pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
    solution(word,pages)
    