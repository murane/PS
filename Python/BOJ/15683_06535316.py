def watch(x, y, directions):
    #x,y좌표에서 directions 방향으로 보자..
    coor_set = set()
    #여러방향을 볼수 있으므로 각 방향을 볼때마다 채워준다
    for d in directions:
        nx, ny = x, y
        #x,y값은 tmp값에 복사하여 보존
        while 1:
            #dx,dy를 통해 방향설정
            nx, ny = dx[d]+nx, dy[d]+ny
            if 0<=nx<n and 0<=ny<m:
                #벽에 막히는경우
                if matrix[nx][ny] == 6:
                    break
                #감시받는 spot의 좌표를 저장
                if matrix[nx][ny] == 0:
                    coor_set.add((nx, ny))
            else:
                break
    #즉 matrix를 복사하여 채우고 확인하지 않고
    #matrix에서 바뀌게될부분을 count하여 좌표set을 return함
    return coor_set

#감시를 수행함
def dfs(cnt, union_set):
    #dfs를 재귀로 수행하기 때문에 depth를 cnt로 표현 초기값 0
    #union_set은 ...
    global max_v
    #모든 cctv를 다 본 상황 
    if cnt == len(all_cctv):
        #제일 많이 채웠을때의 수 global변수 max_v를 갱신한다
        max_v = max(max_v, len(union_set))
        return 

    else:
        for i in all_cctv[cnt]:
            dfs(cnt+1, union_set|i)
    


n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
empty = 0

# 위, 오른쪽, 아래, 왼쪽
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

all_cctv = []
max_v = 0

#matrix를 순회
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0: empty += 1
        #0즉 공백은 empty에 누적
        elif matrix[i][j] == 1: 
            all_cctv.append([watch(i, j, [0]), watch(i, j, [1]), watch(i, j, [2]), watch(i, j, [3])])
        #1일경우 watch 0,1,2,3을 all_cctv에 삽입
        elif matrix[i][j] == 2:
            all_cctv.append([watch(i, j, [0,2]), watch(i, j, [1,3])])
        #2일경우 watch 0,2 1,3을 삽입
        elif matrix[i][j] == 3:
            all_cctv.append([watch(i, j, [0,1]), watch(i, j, [1,2]), watch(i, j, [2,3]), watch(i, j, [3,0])])
        #각각의 방향을 보는것을 append하는듯하다
        elif matrix[i][j] == 4:
            all_cctv.append([watch(i, j, [0,1,2]), watch(i, j, [1,2,3]), watch(i, j, [2,3,0]), watch(i, j, [3,0,1])])

        elif matrix[i][j] == 5:
            all_cctv.append([watch(i, j, [0,1,2,3])])
#matrix를 모두순회하여 각각의 cctv타입에 따라 보는 경우의수를 all_cctv원소로 삽입
#

dfs(0, set())
print(empty-max_v)