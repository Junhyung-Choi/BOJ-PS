import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int,input().split())))
arr.sort(key= lambda x:(x[1],x[0]))
cnt = 0
bs = -1
be = -1
for i in arr:
    ns = i[0]
    ne = i[1]
    if ns >= be:
        bs = ns
        be = ne
        cnt += 1
print(cnt)