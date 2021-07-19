global check,n
check = 0
n = int(input())
result = [0 for _ in range(n*n)]

def division(current, step, result):
    global check, n
    if step > n:
        return
    count = 0
    for i in range(step):
        count += result[i]#result에 있는 값을 전부 확인.
    if count > n:
        return #모두 더한 값이 n보다 크면 종료


    if count == n:
        for i in range(step):
            if i == step - 1:
                print(result[i])
                check += 1 #모든 값을 다 꺼냈으면 check 값을 1올려줌
            else:
                print(result[i], end="") #값을 꺼낸다.
                print("+", end="")
    else:
        for i in range(current, 0, -1):
            result[step] = i
            division(i, step + 1, result)


if 2 <= n <= 20:
    division(n - 1, 0, result)
    print(check)