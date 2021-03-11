#BOJ 1037 - 약수
factornum = int(input())
factors = sorted(list(map(int,input().split())))
print(factors[0] * factors[-1])