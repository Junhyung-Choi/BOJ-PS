#BOJ 1032 - 명령 프롬프트
lines = int(input())

first = input()
check = list(first)
for _ in range(lines-1):
    tmp = input()
    for index in range(len(tmp)):
        if tmp[index] != check[index] and check[index] != '?':
            check[index] = '?'
print(''.join(check))