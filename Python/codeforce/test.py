n, m = map(int, input().split()) # voters, parties
 
money = [0] * n
 
for i in range(n):
    x, y = map(int, input().split())
    money[i] = (y, x - 1)
    #cost, party
money.sort()
 
def calc(lim):
    visited = [False] * n
    cost = 0
 
    cnt = [0] * m
    for i in range(n):
        cnt[money[i][1]] += 1
        #파티별 득표수 체크
    for i in range(n):
        if money[i][1] != 0 and cnt[money[i][1]] >= lim:
        #0번당이 아니고 득표가 lim보다 크거나 같으면..
            cnt[money[i][1]] -= 1
            cnt[0] += 1
            cost += money[i][0]
            visited[i] = True
            #득표를 하나 줄이고 0번에 올린다음에.. 코스트를 하나 가져온다
    for i in range(n):
        if cnt[0] >= lim:
            break
        #한계치를 넘어서면 끝내자
        if money[i][1] != 0 and not visited[i]:
            cnt[money[i][1]] -= 1
            cnt[0] += 1
            cost += money[i][0]
        #0번당이 아니고.. 방문을 안했으면..
        
 
    return cost
 
ans = 10 ** 18
 
for i in range(n):
    ans = min(ans, calc(i))
 
print(ans)