import sys
from string import ascii_lowercase
r=sys.stdin.readline
L=r()
alpastr=r().strip()
res=0
for i,ch in enumerate(alpastr):
    for alpa,v in list(zip(ascii_lowercase,range(1,27))):
        if ch==alpa:
            res+=(v*(31**i))
print(res%1234567891)

