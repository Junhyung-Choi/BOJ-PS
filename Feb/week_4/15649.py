#BOJ 15649 - N과 M(1)
n,m = map(int,input().split())
s = []

def printm():
    if len(s) == m:
        print(' '.join(list(map(str,s))))
        return
    
    else:
        for i in range(1,n+1):
            if i in s:
                continue
            s.append(i)
            printm()
            s.pop()
printm()

