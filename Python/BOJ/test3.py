from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    sumv = 0
    visited = set()
    q = deque()
    q.append((x, y))
    while q:
        node = q.popleft()
        if check[node[0]][node[1]] == 0: continue
        visited.add((node[0], node[1]))
        check[node[0]][node[1]] = 0
        sumv = sumv + city[node[0]][node[1]]

        for i in range(4):
            nx, ny = node[0] + dx[i], node[1] + dy[i]
            if not (0 <= nx < N and 0 <= ny < N): continue
            if check[nx][ny] == 0: continue
            if not (L <= abs(city[node[0]][node[1]] - city[nx][ny]) <= R): continue
            q.append((nx, ny))
    return visited, sumv // len(visited)


if __name__ == '__main__':
    N, L, R = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    while True:
        flag = 0
        check = [[-1]*N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if check[x][y] == 0: continue
                array, change = bfs(x, y)
                if len(array) > 1:
                    flag = 1
                    for i, j in array:
                        city[i][j] = change
        if flag == 0: break
        check.clear()
        cnt = cnt + 1
    print(cnt)