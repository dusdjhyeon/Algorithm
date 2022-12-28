#1541 - 잃어버린 괄호

s = input().split('-')
count = 0

for i in range(len(s)):
    r = s[i].split('+')
    start = int(r[0])
    for j in range(1, len(r)):
        start += int(r[j])
    s[i] = start

num = s[0]
for i in range(1, len(s)):
    num -= s[i]
print(num)