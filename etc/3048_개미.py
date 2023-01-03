#3048 - 개미

import sys
input = sys.stdin.readline

n1, n2 = map(int,input().split())
g1 = list(input().rstrip()) #왼-> 오
g2 = list(input().rstrip()) #오->왼
t = int(input())
ant = g1[::-1]+g2

for i in range(t):
    for j in range(n1+n2-1):
        if ant[j] in g1 and ant[j+1] in g2:
            ant[j], ant[j+1] = ant[j+1], ant[j]

            if ant[j+1] == g1[0]: break
    
print(''.join(ant))