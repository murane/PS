from string import ascii_uppercase
def scan(m, n, tb)->list:
    lst=set()
    for i in range(m-1):
        for j in range(n-1):
            if tb[i][j]==tb[i+1][j+1]==tb[i+1][j]==tb[i][j+1] and tb[i][j] in ascii_uppercase:
                lst.update([(i,j),(i,j+1),(i+1,j),(i+1,j+1)])
    return list(lst)
def down(m,n,board):
    for col in range(n):
        for i in range(m-1,-1,-1):
            for j in range(m-1,0,-1):
                if board[j][col]==" " and board[j-1][col] in ascii_uppercase:
                    board[j][col],board[j-1][col]=board[j-1][col],board[j][col]
    return board
def solution(m, n, board):
    answer = 0
    board=[list(row) for row in board]
    #테이블에서 지워질 칸을 한번에 스캔하여 그 좌표들을 저장한다
    while True:
        lst=scan(m,n,board)
        if not lst: break
        #지운 칸의 갯수를 answer에 저장한다.
        answer+=len(lst)
        #한번에 칸들을 지우고 각 열별로 모든 블록을 바닥으로 내린다.
        for x,y in lst:
            board[x][y]=" "
        board=down(m,n,board)
    #지워질 칸이 없을때까지 반복한다.
    return answer
if __name__ == '__main__':
    m=5
    n=6
    board=["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]
    solution(m,n,board)
    