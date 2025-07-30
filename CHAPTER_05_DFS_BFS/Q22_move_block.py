# https://programmers.co.kr/learn/courses/30/lessons/60063

board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]

def solution(board):
    answer = 0
    n = len(board)
    from collections import deque

    visited_row = [[float('inf')]*n for _ in range(n)]
    visited_col = [[float('inf')]*n for _ in range(n)]

    q = deque([(0,0,1,0,0)])
    
    while q:
        
        x1,y1,x2,y2,sec = q.popleft()
        if x2 == n-1 and y2 == n-1:
            answer = sec
            break

        #move
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx1:=x1+dx) < n and 0 <= (nx2:=x2+dx) < n \
            and  0 <= (ny1:=y1+dy) < n and 0 <= (ny2:=y2+dy) < n :
                if board[ny1][nx1] == 0 and board[ny2][nx2] == 0:
                    nx1,nx2 = min(nx1,nx2),max(nx1,nx2)
                    ny1,ny2 = min(ny1,ny2),max(ny1,ny2)
                    if ny1 == ny2:
                        if visited_row[ny2][nx2] > sec + 1:
                            q.append((nx1,ny1,nx2,ny2,sec+1))
                            visited_row[ny2][nx2] = sec + 1
                    if nx1 == nx2:
                        if visited_col[ny2][nx2] > sec + 1:
                            q.append((nx1,ny1,nx2,ny2,sec+1))
                            visited_col[ny2][nx2] = sec + 1
        #rotate1
        if y1 == y2:
            if 0 <= y1-1:
                nx1,nx2 = min(x1,x2),max(x1,x2)
                if board[y1-1][x1] == 0 and board[y2-1][x2] == 0:
                    if visited_col[y1][x1] > sec + 1:
                        q.append((x1,y1-1,x1,y1,sec+1))
                        visited_col[y1][x1] = sec + 1
                    if visited_col[y2][x2] > sec + 1:
                        q.append((x2,y2-1,x2,y2,sec+1))
                        visited_col[y2][x2] = sec + 1
            if y1+1 < n:
                if board[y1+1][x1] == 0 and board[y2+1][x2] == 0:
                    if visited_col[y1+1][x1] > sec + 1:
                        q.append((x1,y1,x1,y1+1,sec+1))
                        visited_col[y1+1][x1] = sec + 1
                    if visited_col[y2+1][x2] > sec + 1:
                        q.append((x2,y2,x2,y2+1,sec+1))
                        visited_col[y2+1][x2] = sec + 1

        #rotate2
        if x1 == x2:
            y1,y2 = min(y1,y2),max(y1,y2)
            if 0 <= x1-1:
                if board[y1][x1-1] == 0 and board[y2][x2-1] == 0:
                    if visited_row[y1][x1] > sec + 1:
                        q.append((x1-1,y1,x1,y1,sec+1))
                        visited_row[y1][x1] = sec + 1
                    if visited_row[y2][x2] > sec + 1:
                        q.append((x2-1,y2,x2,y2,sec+1))
                        visited_row[y2][x2] = sec + 1
            if x1+1 < n:
                if board[y1][x1+1] == 0 and board[y2][x2+1] == 0:
                    if visited_row[y1][x1+1] > sec + 1:
                        q.append((x1,y1,x1+1,y1,sec+1))
                        visited_row[y1][x1+1] = sec + 1
                    if visited_row[y2][x2+1] > sec + 1:
                        q.append((x2,y2,x2+1,y2,sec+1))
                        visited_row[y2][x2+1] = sec + 1

    return answer

print(solution(board))
