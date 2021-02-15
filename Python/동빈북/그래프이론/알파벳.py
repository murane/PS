import sys
input = sys.stdin.readline
 
def bfs():
    mx = 0
    queue = set()
    queue.add((0, 0, board[0][0]))
 
    while queue:
        x, y, sentence = queue.pop()
        mx = max(mx, len(sentence))
        if mx == 26: return 26
        ## 동 남 서 북
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if board[nx][ny] in sentence: continue
            queue.add((nx, ny, sentence + board[nx][ny]))
    return mx
 
 
if __name__ == '__main__':
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]
 
    ## 동 남 서 북
    dxs = (0, 1, 0, -1)
    dys = (1, 0, -1, 0)
    print(bfs())
