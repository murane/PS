from string import digits
def solution(s):
    answer = ''
    start=True
    s=s.lower()
    for i,ch in enumerate(s):
        if start:
            if ch == " ":
                answer+=ch
            elif ch in digits:
                answer+=ch
                start=False
            else:
                answer+=ch.upper()
                start=False
        else:
            answer+=ch
            if i<len(s)-2 and s[i+1]==" ":
                start=True
    return answer

if __name__ == '__main__':
    s="3people unFollowed me"
    solution(s)
    