from collections import Counter
def game(num,candi):
    cnt_s=0
    n_counter,candi_counter=Counter(),Counter()
    for a,b in zip(str(num),str(candi)):
        if a==b:
            cnt_s+=1
        else:
            n_counter[a]+=1
            candi_counter[b]+=1
    cnt_b=len(n_counter&candi_counter)
    return (cnt_s,cnt_b)
game(123,114)