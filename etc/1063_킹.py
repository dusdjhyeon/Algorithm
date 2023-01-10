#1063 - 킹

import sys
input = sys.stdin.readline

king, stone, n = input().rstrip().split()
move = {'R':[1,0],'L':[-1,0], 'B':[0,-1], 'T':[0,1], 'RT':[1,1], 'LT':[-1,1],'RB':[1,-1],'LB':[-1,-1]}
k = [ord(king[0])-64, int(king[1])]
s = [ord(stone[0])-64, int(stone[1])]

for _ in range(int(n)):
    m = input().rstrip()
    nx = k[0] + move[m][0]
    ny = k[1] + move[m][1]

    if 0<nx<=8 and 0<ny<=8:
        if nx == s[0] and ny==s[1]: # 돌이 있는 방향으로 이동 시
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            if 0<sx<=8 and 0<sy<=8:
                k=[nx,ny]
                s=[sx,sy]
        else:
            k=[nx,ny]

print(f'{chr(k[0]+64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')