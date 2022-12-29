#21921번 - 블로그

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

if max(visitor) == 0:
    print("SAD")
else:
    value = sum(visitor[:x])
    max = value
    count = 1
    
    for i in range(x, n):
        value += (visitor[i] - visitor[i-x])

        if(value > max):
            max = value
            count=1
        elif(value == max):
            count+=1

    print(max)
    print(count)