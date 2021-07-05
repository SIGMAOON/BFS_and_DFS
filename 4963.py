# 섬의 개수
# 1은 땅, 0은  바다
# 가로 세로 대각선 이어져있으면 하나의 섬
import sys
from collections import deque
input = sys.stdin.readline

while True:
    cnt = 0
    w,h = map(int,input().split())      

    if w == 0 and h == 0:
        exit()
    island = [list(map(int,input().split())) for _ in range(h)]

    q = deque()
    dx = [0,0,1,1,1,-1,-1,-1]
    dy = [1,-1,0,1,-1,0,1,-1]

    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                q.append((i,j))
                island[i][j] = 2

                while q:
                    x,y = q.popleft()

                    for k in range(len(dx)):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0<=nx<h and 0<=ny<w and island[nx][ny] == 1:
                                q.append((nx,ny))
                                island[nx][ny] = 2
                        
                else:
                    cnt+=1
    print(cnt)

    """while - else 혹은 for - else 문은 해당 반복문이 끝까지 돌면 else 문 실행해줌"""