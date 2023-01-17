#14501 - 퇴사
#다이나믹 프로그래밍, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

n = int(input())
schedule = []
dp = [0 for _ in range(n+1)]

for _ in range(n):
    schedule.append(list(map(int, input().rstrip().split()))) 

for i in range(n):
    dp[i+1] = max(dp[i], dp[i+1])

    if i+schedule[i][0]<=n:
        dp[i+schedule[i][0]] = max(dp[i]+schedule[i][1], dp[i+schedule[i][0]])

print(dp[n])