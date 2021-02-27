#BOJ 15650 - N과 M(2)
n,m = map(int,input().split())
s = []

def printm(start):
    if len(s) == m:
        print(' '.join(list(map(str,s))))
        return
    
    else:
        for i in range(start,n+1):
            if i in s:
                continue
            s.append(i)
            printm(i+1)
            s.pop()
printm(1)