#BOJ 4948 - 베르트랑 공준
prime = [False,True] + [True] * 250000
for i in range(2,250002):
    if prime[i]:
        j = i * 2
        while j < 250002:
            prime[j] = False
            j += i

num = int(input())
while num != 0:
    sum = 0
    for i in range(num+1,2 * num + 1):
        if prime[i]:
            sum += 1
    print(sum)
    num = int(input())