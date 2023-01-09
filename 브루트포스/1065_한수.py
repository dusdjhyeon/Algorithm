#1065 - 한수

import sys
input = sys.stdin.readline

n = int(input())
count = 0

for i in range(1, n+1):
    each = list(map(int, str(i)))
    if i<100:
        count+=1
    elif each[0]-each[1]==each[1]-each[2]:
        count+=1
print(count)