#scofe_2nd 1 - 오디션 연습
import sys
input = sys.stdin.readline

playlistlen, playtime = input().rstrip().split()
playlistlen = int(playlistlen)
ph,pm,ps = map(int,playtime.split(":"))
total = int(ph) * 3600 + int(pm) * 60 + ps
playlist = []
result = [0,]
for _ in range(playlistlen):
    inm,ins = map(int,input().rstrip().split(":"))
    playlist.append(inm*60 + ins)

for index in range(playlistlen):
    sum = 0
    for j in range(index,playlistlen):
        sum += playlist[j]
        if sum >= total:
            result.append(j - index + 1)
            break

m = max(result)
pos = result.index(m)
print(m,pos)