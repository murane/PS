from string import digits
def findIdx(string):
    start=0
    end=0
    for i in range(len(string)):
        if string[i] in digits:
            if start==0:
                start=i
                end=i
            elif i-start<5:
                end=i
        elif start!=0:
            break
    return start,end
def solution(files):
    lst = []
    for file in files:
        s,e=findIdx(file)
        head,number,origin=file[:s].lower(),int(file[s:e+1]),file
        lst.append([head,number,origin])
    lst.sort(key=lambda x: (x[0],x[1]))
    return [x[2] for x in lst]
if __name__ == '__main__':
    files=["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    solution(files)
    