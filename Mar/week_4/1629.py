#BOJ 1629 - 곱셈
# (a+b)%m = ((a%m)+(b%m)) % m
# (a*b)%m = ((a%m)*(b%m)) % m
# (a-b)%m = ((a%m)-(b%m)+m) % m // 음수가 나올 수 있음

a,b,c = map(int,input().split())
def getCloser(moda, pownum):
    if pownum == 0:
        return 1
    elif pownum == 1:
        return moda
    if (pownum % 2) > 0:
        return getCloser(moda, pownum - 1) * moda
    half = (getCloser(moda, pownum // 2) % c)
    return (half * half) % c
print(getCloser(a,b) % c)

