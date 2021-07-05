# DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline
v,e,start = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i].sort()
    graph[j].sort()

visited = [0]*(v+1)

def DFS(node):
    visited[node] = 1
    print(node,end =' ')
    for n in graph[node]:
        if visited[n] == 0:
            visited[n] = 1
            DFS(n)


def BFS(node):
    q = deque()
    q.append(node)
    visited[node] = 1
    while q:
        a = q.popleft()
        print(a,end=' ')
        for n in graph[a]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = 1

DFS(start)
print()
visited = [0]*(v+1)
BFS(start) 