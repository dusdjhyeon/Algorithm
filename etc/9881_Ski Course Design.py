#9881 - Ski Course Design

import sys
input = sys.stdin.readline

def cost(low, height):
    count = 0
    for h in height:
        if h<low:
            count+=(low-h)**2
        elif h>low+17:
            count+=(h-(low+17))**2
    return count

n = int(input())
height = [int(input()) for _ in range(n)]
high = max(height)
low = min(height)

if high-low <= 17:
    print(0)
else:
    print(min(cost(c, height) for c in range(low, high-17)))