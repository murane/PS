from string import ascii_lowercase,digits
def solution(new_id:str):
    #1단계
    new_id=new_id.lower()
    #2단계
    tmp=""
    for i in range(len(new_id)):
        if new_id[i] in ascii_lowercase+digits+"-_.":
            tmp+=new_id[i]
    new_id=tmp
    #3단계
    while new_id.find('..')!=-1:
        new_id=new_id.replace('..','.')
    #4단계
    if new_id and new_id[0]==".":
        new_id=new_id[1:]
    if new_id and new_id[-1]==".":
        new_id=new_id[:-1]
    #5단계
    if new_id=="":
        new_id+="a"
    #6단계
    if len(new_id)>=16:
        new_id=new_id[:15]
        if new_id[-1]==".":
            new_id=new_id[:-1]
    #7단계
    if len(new_id)<=2:
        new_id=new_id+new_id[-1]*(3-len(new_id))
    return new_id