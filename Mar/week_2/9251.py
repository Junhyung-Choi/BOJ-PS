#BOJ 9251 - LCS
fstring = input()
sstring = input()
flen = len(fstring)
slen = len(sstring)
dp = [[0] * (flen + 1) for _ in range(slen + 1)]

for y in range(1,slen + 1):
    for x in range(1,flen + 1):
        if fstring[x-1] == sstring[y-1]:
            dp[y][x] = dp[y-1][x-1] + 1
        else:
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])
print(dp[slen][flen])
