#BOJ 2096 - 내려가기
import sys
input = sys.stdin.readline

lines = int(input())
max_line = min_line = list(map(int,input().split()))

for index in range(lines-1):
    line = list(map(int,input().split()))
    max_line = [line[0] + max(max_line[0],max_line[1]), line[1] + max(max_line), line[2] + max(max_line[1],max_line[2])]
    min_line = [line[0] + min(min_line[0],min_line[1]), line[1] + min(min_line), line[2] + min(min_line[1],min_line[2])]

print(max(max_line),min(min_line))