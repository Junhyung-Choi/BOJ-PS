#BOJ 1927 - 최소 힙
import sys
input = sys.stdin.readline

minHeap = []
C = int(input())

def swap(a,b):
    minHeap[a],minHeap[b] = minHeap[b],minHeap[a]

def delete():
    if minHeap == []:
        print(0)
    elif len(minHeap) == 1:
        print(minHeap.pop())
    else:
        tmp = minHeap.pop()
        print(minHeap[0])
        minHeap[0] = tmp
        pidx = 0
        while pidx < len(minHeap):
            lcidx = pidx * 2 + 1
            rcidx = pidx * 2 + 2
            if lcidx >= len(minHeap):
                break
            elif rcidx >= len(minHeap):
                if minHeap[pidx] > minHeap[lcidx]:
                    swap(pidx,lcidx)
                break
            if minHeap[pidx] < minHeap[rcidx] and minHeap[pidx] < minHeap[lcidx]:
                break
            else:
                smaller = lcidx if minHeap[lcidx] <= minHeap[rcidx] else rcidx
                if minHeap[pidx] > minHeap[smaller]:
                    swap(pidx,smaller)
                    pidx = smaller
                else:
                    break

def add(num):
    minHeap.append(num)
    cidx = len(minHeap)-1
    while cidx > 0:
        if cidx % 2 == 0:
            pidx = (cidx - 2) // 2
        else:
            pidx = (cidx - 1) // 2
        if minHeap[pidx] > minHeap[cidx]:
            swap(pidx,cidx)
            cidx = pidx
        else:
            break


for _ in range(C):
    cmd = int(input())
    if cmd == 0 :
        delete()
    else:
        add(cmd)
