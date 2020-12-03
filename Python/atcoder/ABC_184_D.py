import sys
r=sys.stdin.readline
A,B,C=map(int,r().split())
ans=0
za,mo=0,0
mo=A+B+C

za=A
tmp=za/mo*(100-za)
ans+=(tmp)

za=B
tmp=za/mo*(100-za)
ans+=(tmp)

za=C
tmp=za/mo*(100-za)
ans+=(tmp)

print(f'{ans:.9f}')
