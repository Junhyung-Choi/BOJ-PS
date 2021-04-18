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
    side, poly = map(int,input().split())
    gnum = math.gcd(side,poly)
    side = side // gnum
    poly = poly // gnum
    yuk = bigSqaure(side,mod-2)
    result += (poly * yuk)
    result = result % mod

print(result)