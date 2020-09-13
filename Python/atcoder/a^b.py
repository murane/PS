def pow(a,b):
    res=1
    for _ in range(b):
        res*=a
    return res

def powDAC(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    elif b%2==0:
        tmp=powDAC(a,b/2)
        return tmp**2
    else:
        return a*powDAC(a,b-1)