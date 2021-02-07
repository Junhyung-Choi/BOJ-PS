#BOJ 1931 - 회의실 배정
import sys
input = sys.stdin.readline

C = int(input())
conferlist = []

for _ in range(C):
    conferlist.append(tuple(map(int,input().split())))

conferlist.sort(key= lambda confertime:(confertime[1],confertime[0]))

count = 0

lend = -1

for confertime in conferlist:
    pstart = confertime[0]
    pend = confertime[1]
    if pstart >= lend:
        lend = pend
        count += 1

print(count)