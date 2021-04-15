#BOJ 13172 - Σ
import sys,math
input = sys.stdin.readline

mod = 1000000007

dicenum = int(input())


def bigSqaure(num,sqnum):
    if sqnum == 1:
        return num
    if sqnum % 2 == 1:
        return num * bigSqaure(num,sqnum - 1) % mod
    half = bigSqaure(num,sqnum // 2)
    return (half * half) % mod

result = 0

for _ in range(dicenum):
    side, polysum = map(int,input().split())
    side = side // math.gcd(side,polysum)
    polysum = polysum // math.gcd(side,polysum)
    yuk = bigSqaure(side,mod-2)
    result += (polysum * yuk) % mod
    result = result % mod

print(result)