def is_list_range(row, col):
    return row >= 0 and row < N and col >= 0 and col < N

def solve():
    global sharks, board, smell, M
    
    # 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
    for key in sharks.keys():
        row, col = sharks[key][0], sharks[key][1]
        smell[row][col] = [key,K]

    # 1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다.
    count = 0
    while True:
        # 1번 상어만 남아있는지 확인
        if M == 1:
            return count
        print("cur>>")
        # 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고,
        for key in sharks.keys():
            direction = priority[key][sharks[key][2]]
            now_row, now_col = sharks[key][0], sharks[key][1]
            check = False
            # 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
            for i in direction:
                next_row, next_col = now_row + dr[i], now_col + dc[i]
                if is_list_range(next_row, next_col) and smell[next_row][next_col] == [0,0]:
                    sharks[key][0] = next_row
                    sharks[key][1] = next_col
                    sharks[key][2] = i
                    check = True
                    break

            if check:
                continue

            # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 
            for i in direction:
               next_row, next_col = now_row + dr[i], now_col + dc[i]
               if is_list_range(next_row, next_col) and smell[next_row][next_col][0] == key:
                   sharks[key][0] = next_row
                   sharks[key][1] = next_col
                   sharks[key][2] = i
                   break
        for k,v in sharks.items():
            print(f'{k}, {v} ')
        # 한 칸에 상어가 겹쳐있는지 확인한다.
        sharks_keys = sorted(sharks.keys())
        for key in sharks_keys:
            if sharks.get(key) is not None:
                for next_key in sharks_keys:
                    if key == next_key:
                        continue
                    if sharks.get(next_key) is not None:
                        if (sharks[key][0],sharks[key][1]) == (sharks[next_key][0],sharks[next_key][1]):
                            delete_key = max(key,next_key)
                            del sharks[delete_key]
                            M -= 1

        # 냄새를 -1씩 해준다.
        for i in range(N):
            for j in range(N):
                if smell[i][j][1] != 0:
                    smell[i][j][1] -= 1
                    if smell[i][j][1] == 0:
                        smell[i][j] = [0,0]
        
        # 냄새를 뿌린다.
        for key in sharks.keys():
            row, col = sharks[key][0], sharks[key][1]
            smell[row][col] = [key,K]

    
        # 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1
        count += 1
        if count > 1000:
            return -1
        

N, M, K = map(int,input().split())

sharks = dict()

board = []

smell = [[[0,0] for _ in range(N)] for _ in range(N)]

for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] != 0:
            sharks[board[i][j]] = [i,j]

start_direction = list(map(int,input().split()))

for i in range(len(sharks.keys())):
    sharks[i+1].append(start_direction[i])

#우선순위
priority = [[] for _ in range(M+1)]
for i in range(1,M+1):
    priority[i].append([])
    for _ in range(4):
        priority[i].append(list(map(int,input().split())))

# x, 위, 아래, 왼쪽, 오른쪽
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

result = solve()
print(result)