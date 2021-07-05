# 바닥 장식
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
bang = [list(input())[:-1] for _ in range(n)]

garo = 0
saero = 0

q = deque()

dx = [1,0]
dy = [0,1]

q = deque()

# 가로 타일
for i in range(n):
    for j in range(m):
        if bang[i][j] == '-':
            garo+=1
            q.append((i,j))
            bang[i][j] == '.'

            while q:
                x,y = q.popleft()

                nx = x + dx[1]
                ny = y + dy[1]

                if 0<=nx<n and 0<=ny<m and bang[nx][ny]=='-':
                    q.append((nx,ny))
                    bang[nx][ny] = '.'
                    
        elif bang[i][j] == '|':
            saero+=1
            q.append((i,j))
            bang[i][j] == '.'

            while q:
                x,y = q.popleft()

                nx = x + dx[0]
                ny = y + dy[0]

                if 0<=nx<n and 0<=ny<m and bang[nx][ny]=='|':
                    q.append((nx,ny))
                    bang[nx][ny] = '.'

print(garo+saero)