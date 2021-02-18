#BOJ 1107 - 리모컨
destination = int(input())
btnnum = int(input())
if btnnum != 0:
    btnlist = list(map(str,input().split()))
cnt = abs(destination - 100)

for newchannel in range(1000001):
    check = True
    newchannel = str(newchannel)
    for num in range(len(newchannel)):
        if btnnum != 0 and newchannel[num] in btnlist:
            check = False
            break
    if check:
        cnt = min(cnt,abs(destination - int(newchannel))+len(newchannel))
print(cnt)
