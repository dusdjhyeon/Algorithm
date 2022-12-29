#19941번 - 햄버거 분배

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
location = list(input())
ans = 0

for i in range(n):
    if location[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if location[j] == 'H':
                location[j] = 0
                ans += 1
                break
print(ans)