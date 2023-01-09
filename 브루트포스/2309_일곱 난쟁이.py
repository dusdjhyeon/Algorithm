#2309 - 일곱 난쟁이

import sys
import itertools
input = sys.stdin.readline

height = [int(input()) for _ in range(9)]

height.sort()

for i in itertools.combinations(height, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break