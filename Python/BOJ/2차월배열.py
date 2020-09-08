test=[
    '0011',
    '0110',
    '1001'
]
pattern = [
    '01',
    '10'
]
for i in range(len(test)-len(pattern)+1):
    for j in range(len(test[0])-len(pattern[0])+1):
        for p in range(len(pattern)):
            for q in range(len(pattern[0])):
                if test[i+p][j+q]==pattern[p][q]:
                    print(f'{pattern[p][q]} ',end="")
                else:
                   print(f'x ',end="")
            print("")
        print("--------------")