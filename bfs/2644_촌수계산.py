#2644번 - 촌수계산

import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
  queue = deque()
  queue.append(node)

  while queue:
    node = queue.popleft()
    for i in graph[node]:
      if check[i] == 0:
        check[i] = check[node]+1
        queue.append(i)

n = int(input())
a,b = map(int, input().split()) 
m = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(m):
  u,v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

check = [0]*(n+1)
bfs(a)
print(check[b] if check[b] > 0 else -1)