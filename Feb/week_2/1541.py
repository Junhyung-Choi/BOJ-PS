#BOJ 1541 - 잃어버린 괄호
exp = input().rstrip()
tmpnum = ""
arr = []
sum = 0
check = False
for i in exp:
    if ord(i) == 43 or ord(i) == 45:
        arr.append(int(tmpnum))
        tmpnum = ""
        arr.append(i)
    else:
        tmpnum += i
arr.append(int(tmpnum))
for i in arr:
    if type(i) == int:
        if not check :
            sum += i
        else:
            sum -= i
    else:
        if i == "-":
            check = True
print(sum)