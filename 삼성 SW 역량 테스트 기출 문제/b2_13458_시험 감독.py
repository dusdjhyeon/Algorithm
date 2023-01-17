#13458 - 시험 감독
#수학, 사칙연산

import sys
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rstrip().split()))
b,c = map(int, input().rstrip().split())
director = 0

for i in a:
    i-=b
    if i>0:
        director += math.ceil(i/c)
    director+=1
print(director)