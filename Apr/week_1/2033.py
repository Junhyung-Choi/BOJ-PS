#BOJ 2033 - 반올림
n = int(input())
comp = 10
i = 1
while True:
    if n > comp:
        tmp = (n % comp) // (comp // 10)
        if tmp >= 5:
            n = (n // comp) * comp + comp
        else:
            n = (n // comp) * comp
    else:
        break
    comp *= 10
    i += 1
print(n)