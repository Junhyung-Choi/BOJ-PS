#BOJ 12865 - 평범한 배낭
import sys
input = sys.stdin.readline

itemnum, max_weight = map(int,input().split())
items = []

for _ in range(itemnum):
    items.append(list(map(int,input().split())))

#items.sort(key = (lambda x : x[0]))
dp = [[0] * (max_weight + 1) for _ in range(itemnum + 1)]

for item in range(1,itemnum + 1):
    print("Current item",items[item-1])
    for weight in range(1,max_weight + 1):
        print("Current weight", weight)
        iwgt = items[item-1][0]
        ival = items[item-1][1]
        if iwgt <= weight:
            print("ival + dp[item-1][weight - iwgt]",ival + dp[item-1][weight - iwgt])
            print("dp[item-1][weight]",dp[item-1][weight])
            dp[item][weight] = max(ival + dp[item-1][weight - iwgt],dp[item-1][weight])
        else:
            dp[item][weight] = dp[item-1][weight]
print(dp)
print(dp[itemnum][max_weight])