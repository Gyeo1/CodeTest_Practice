## template
a = [[int(x) for x in input().split()] for i in range(9)]
b = 0
count = 0
check = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if 1 <= a[i][j] < 100:
            count += 1
if count == 81:
    count = 0
    for i in range(len(a)):
        check.append(max(a[i]))
    for i in range(len(check)):
        count = check[i]
        if count == max(check):
            print(count)
            b = i
            break
    for i in range(len(a[b])):
        if a[b][i] == count:
            print(b + 1, end=" ")
            print(i + 1)
            break
