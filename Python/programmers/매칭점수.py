import re
from operator import itemgetter
from collections import defaultdict
def solution(word, pages):
    tb=dict()
    default_stat=dict()
    link_stat=dict()
    matching_stat=defaultdict(float)
    word=word.lower()
    for i in range(len(pages)):
        pages[i]=pages[i].lower()
    for i,page in enumerate(pages):
        url=re.search(r'<meta property="og:url" content=\"(\S*)\"/>', page).group(1)
        tb[url]=i
        tb[i]=url
        cnt=re.sub('[^a-z]','.',page).split(".").count(word)
        default_stat[i]=cnt
        links=re.findall(r'<a href=\"(\S*)\">',page)
        link_stat[i]=links
    for i in range(len(pages)):
        #i번째 페이지에서
        for link in link_stat[i]:
            #각 링크별로
            if link in tb:
                #테이블에 존재하는 링크면
                #해당 링크의 매칭점수에 현재 페이지의 링크점수를 더해준다
                matching_stat[tb[link]]+=(default_stat[i]/len(link_stat[i]))
        matching_stat[i]+=default_stat[i]
    res = list(matching_stat.items())
    res.sort(key=lambda x:(x[1],-x[0]),reverse=True)
    return res[0][0]

if __name__ == '__main__':
    word="Muzi"
    pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
    solution(word,pages)
    