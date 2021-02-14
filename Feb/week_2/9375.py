#BOJ 9375 - 패션왕 신해빈
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    d = {}
    C = int(input())
    sum = 0
    for each in range(C):
        name,kind = input().split()
        if kind not in d.keys():
            d[kind] = [name]
        else:
            d[kind].append(name)
    if C == 0:
        print(0)
    else:
        sum = 1
        for k in d.keys():
            sum = sum * (len(d[k]) + 1)
        sum -= 1
        print(sum)
    