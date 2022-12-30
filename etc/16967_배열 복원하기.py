#16967번 - 배열 복원하기

import sys
input = sys.stdin.readline

h,w,x,y = map(int, input().rstrip().split())
B = [list(map(int, input().rstrip().split())) for _ in range(h+x)]

A = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    A[i] = B[i][:w]

for i in range(x,h):
    for j in range(y,w):
        A[i][j] = B[i][j] - A[i-x][j-y]

for i in range(h):
  for j in range(w):
    print(A[i][j],end=" ")
  print("")
  