#15059 - Hard choice

import sys
from collections import deque
input = sys.stdin.readline

ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())
ans = max(0, cr-ca) + max(0, br-ba) + max(0, pr-pa)
print(ans)