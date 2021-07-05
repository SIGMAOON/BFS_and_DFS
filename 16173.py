# 점프왕 쩰리 (Small)
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]

    visit = [[0]*n for _ in range(n)]

    q = deque()
    dx,dy = [1,0],[0,1]
    q.append([0,0])

    while q:
        x,y = q.popleft()

        jump = board[x][y]

        if jump == -1:
            return True
    
        for i in range(2):
            nx = x + dx[i]*jump
            ny = y + dy[i]*jump

            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append([nx,ny])

    return False

if bfs():
    print("HaruHaru")
else:
    print("Hing")