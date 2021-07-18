## template
str1 = input()
i = 0
j = 1
count = 1
if 1 <= len(str1) <= 1000:
    while (1):
        if str1[i] == str1[j]:
            count += 1
        else:
            if count != 1:
                print(count, end="")
            print(str1[i], end="")
            count = 1
            i = j
        j += 1
        if j == len(str1):
            if count != 1:
                print(count, end="")
            print(str1[i], end="")
            break
