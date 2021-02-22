#BOJ 3009 - 네 번째 점
xarr = []
yarr = []
for _ in range(3):
    tx,ty = map(int,input().split())
    xarr.append(tx)
    yarr.append(ty)
rx,ry = 0,0

if xarr[0] == xarr[1]:
    rx = xarr[2]
elif xarr[0] == xarr[2]:
    rx = xarr[1]
else:
    rx = xarr[0]

if yarr[0] == yarr[1]:
    ry = yarr[2]
elif yarr[0] == yarr[2]:
    ry = yarr[1]
else:
    ry = yarr[0]
print(rx,ry)