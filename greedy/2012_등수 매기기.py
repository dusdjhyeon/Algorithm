#1459 - 등수 매기기

import sys
input = sys.stdin.readline

n= int(input())
rank = []
result = 0
for _ in range(n):
    rank.append(int(input().rstrip()))
rank.sort()

for i in range(1, n+1):
    result += abs(i-rank[i-1])

print(result)