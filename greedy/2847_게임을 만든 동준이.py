#2847번 - 게임을 만든 동준이

N = int(input()) #레벨의 수
M = [] #점수

for i in range(N):
    M.append(int(input()))

M.reverse()
count = 0

for i in range(N-1):
    if M[i]<=M[i+1]:
        while(M[i]<=M[i+1]):
            M[i+1]-=1
            count+=1

print(count)