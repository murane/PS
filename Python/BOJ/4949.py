import sys
r=sys.stdin.readline
tmp=''
while True:
    sentence = r().replace('\n','')
    if sentence=='.':
        break
    else:
        #다음줄이 있다
        if sentence[-1]!='.':
            tmp+=sentence
        #다음은 없다
        else:
            tmp+=sentence
            flg=True
            stack=[]
            for ch in tmp:
                if ch=='(' or ch=='[':
                    stack.append(ch)
                elif ch==')':
                    if stack and stack[-1]=='(':
                        stack.pop()
                    else:
                        flg=False
                        break
                elif ch==']':
                    if stack and stack[-1]=='[':
                        stack.pop()
                    else:
                        flg=False
                        break
            if flg and len(stack)==0:
                print("yes")
            else:
                print("no")
            tmp=''
