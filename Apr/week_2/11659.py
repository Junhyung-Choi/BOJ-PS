#BOJ 11659 - 구간 합 구하기 4
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
numlist = list(map(int,input().split()))
sumlist = [0] * n
for i in range(n):
	sumlist[i] = numlist[i] + sumlist[i-1]
for _ in range(m):
	start, end = map(int,input().split())
	print(sumlist[end-1] - sumlist[start-1] + numlist[start-1])
