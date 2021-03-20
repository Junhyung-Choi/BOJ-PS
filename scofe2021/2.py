#Scofe 2 - 배송 전략 실험
length = int(input())
data = list(map(int,input()))
dp = [0,1,1,2]
for i in range(4,51):
    dp.append(dp[i-1]+dp[i-2])

cnt = 0
result = 1
for road in data:
    if road == 0:
        result *= dp[cnt]
        cnt = 0
    else:
        cnt += 1
result *= dp[cnt]
print(result)