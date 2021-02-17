#BOJ 11047 - 동전 0
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []
sum = 0
for i in range(n):
    coins.append(int(input()))

for i in range(n-1,-1,-1):
    if k >= coins[i]:
        sum += k // coins[i]
        k = k % coins[i]
    if k == 0:
        break

print(sum)