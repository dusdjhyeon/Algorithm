#1789 - 수들의 합

import sys
input = sys.stdin.readline

s = int(input())
n = 0

while (n+1)*n /2 <=s:
    n+=1

print(n-1)