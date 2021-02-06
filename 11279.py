import sys
input = sys.stdin.readline

maxHeap = []
C = int(input())

def delete():
    if maxHeap == []:
        print(0)
    elif len(maxHeap) == 1:
        print(maxHeap.pop())
    else:
        tmp = maxHeap[0]
        print(tmp)
        maxHeap[0] = maxHeap.pop()
        pidx = 0
        while True:
            lcidx = pidx * 2 + 1
            rcidx = pidx * 2 + 2
            #그냥 멈추기
            if lcidx >= len(maxHeap):
                break
            #왼쪽만 비교하고 끝내기
            elif rcidx >= len(maxHeap): 
                if maxHeap[pidx] >= maxHeap[lcidx]:
                    break
                else:
                    tmp = maxHeap[pidx]
                    maxHeap[pidx] = maxHeap[lcidx]
                    maxHeap[lcidx] = tmp
                    pidx = lcidx
            #양쪽 다 비교하기
            else:
                if maxHeap[pidx] >= maxHeap[lcidx] and maxHeap[pidx] >= maxHeap[rcidx]:
                    break
                elif maxHeap[pidx] < maxHeap[lcidx] or maxHeap[rcidx]:
                    if maxHeap[lcidx] >= maxHeap[rcidx]:
                        bigger = lcidx
                    else:
                        bigger = rcidx
                    tmp = maxHeap[pidx]
                    maxHeap[pidx] = maxHeap[bigger]
                    maxHeap[bigger] = tmp
                    pidx = bigger

def add(num):
    maxHeap.append(num)
    cidx = len(maxHeap) - 1
    while True:
        if cidx == 0:
            break
        if cidx % 2 == 0:
            pidx = ((cidx - 2) // 2)
        else:
            pidx = ((cidx - 1) // 2)
        if maxHeap[pidx] < maxHeap[cidx]:
            tmp = maxHeap[pidx]
            maxHeap[pidx] = maxHeap[cidx]
            maxHeap[cidx] = tmp
            cidx = pidx
        else:
            break

for _ in range(C):
    cmd = int(input())
    if cmd == 0:
        delete()
    else:
        add(cmd)
