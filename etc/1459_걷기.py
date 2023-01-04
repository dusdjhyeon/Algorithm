#1459 - 걷기

import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().rstrip().split())

#평행으로만 이동
m1 = (x+y)*w

#대각선을 최대한 많이 사용해 이동
if(x+y)%2 == 0:
    m2 = max(x,y)*s
else:
    m2 = w + (max(x,y)-1)*s

#대각선 + 평행 이동
m3 = min(x,y)*s + abs(x-y)*w

print(min(m1,m2,m3))