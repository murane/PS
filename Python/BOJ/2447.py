import sys
r=sys.stdin.readline
N=int(r())
skeleton=[
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
]
base=[
    [['*'],['*'],['*']],
    [['*'],[''],['*']],
    [['*'],['*'],['*']]
]
def print_pattern(p):
    
while N>0:
    if N==3:
        print_pattern(base)
