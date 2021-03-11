#BOJ 2981 - 검문
import sys
import math
input = sys.stdin.readline
num = int(input())
data = []
result = []
for _ in range(num):
    data.append(int(input()))
data.sort()
factor = data[1] - data[0]
for i in range(2,num):
    factor = math.gcd(factor,data[i] - data[i-1])
result.append(factor)
for i in range(2,int(factor**0.5)+1):
    if factor % i == 0:
        if factor // i == i:
            result.append(i)
        else:
            result.append(i)
            result.append(factor // i)
result.sort()
for ans in result:
    print(ans,end = ' ')