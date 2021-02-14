#BOJ 5525 - IOIOI
import sys
input = sys.stdin.readline

n = int(input())
slen = int(input())
s = input().rstrip()
i = 0
ioi = 0
ans = 0 
while i < slen - 2:
    if s[i] == "I" and s[i+1] == "O" and s[i+2] == "I":
        ioi += 1
        if ioi == n:
            ioi -= 1
            ans += 1
        i += 1
    else:
        ioi = 0
    i += 1
print(ans)