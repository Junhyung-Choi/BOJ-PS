n = int(input())
arr = list(map(int, input().split()))
aset = list(sorted(set(arr)))
dic = {}
for i in range(len(aset)):
    dic[aset[i]] = i
for i in arr:
    print(dic[i],end=" ")