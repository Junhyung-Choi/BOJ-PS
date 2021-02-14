#BOJ 18870 - 좌표압축
n = int(input())
dots = list(map(int, input().split()))
dotset = list(sorted(set(dots)))
dotdic = {}
for i in range(len(dotset)):
    dotdic[dotset[i]] = i
for i in dots:
    print(dotdic[i],end=" ")