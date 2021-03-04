#BOJ 1904 - 01타일

pivo = [1,2]
n = int(input())
for i in range(2,n):
    pivo.append((pivo[i-2] + pivo[i-1]) % 15746)
print(pivo[n-1])