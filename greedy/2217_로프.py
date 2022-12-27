#2217번 - 로프

N = int(input()) #N개의 로프
M = [] #로프의 최대 중량 리스트

for i in range(N):
    M.append(int(input()))

M.sort(reverse=True)
result = []

for i in range(N):
    result.append(M[i]*(i+1))

print(max(result))