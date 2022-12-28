#1541 - 잃어버린 괄호

s = input().split('-')
part = sum(map(int, s[0].split('+')))

for i in range(1, len(s)):
    part -= sum(map(int, s[i].split('+')))

print(part)