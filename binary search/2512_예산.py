#2512 - 예산

import sys
input = sys.stdin.readline

n = int(input())
ex = list(map(int, input().rstrip().split()))
m = int(input())

start, end = 0, max(ex)

if sum(ex)<=m:
    print(max(ex))
else:
    while(start<=end):
        mid = (start+end)//2

        total = 0
        for i in ex:
            total+=min(mid, i)

        if total>m:
            end = mid-1
        else:
            start = mid+1
    print(end)