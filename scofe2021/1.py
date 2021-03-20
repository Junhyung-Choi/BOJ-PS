#Scofe 1 - 대여시간을 추천해드립니다.
import sys
input = sys.stdin.readline
num = int(input())
timearr = []
start = 0
end = 1439
def toTimeFormat(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)

for _ in range(num):
    time = list(map(str,input().split()))
    curstart = int(time[0][:2]) * 60 + int(time[0][3:])
    curend = int(time[2][:2]) * 60 + int(time[2][3:])
    start = max(curstart,start)
    end = min(curend,end)
if start > end :
    print(-1)
else:
    shour = toTimeFormat(start // 60)
    smin = toTimeFormat(start % 60)
    ehour = toTimeFormat(end // 60)
    emin = toTimeFormat(end % 60)
    print(shour+":"+smin+" ~ "+ehour+":"+emin)
    
