## template]
C, R = map(int, input().split())  # C는 가로 R은세로
col = 0
row = 0
row_check = []
check = []
count = 0
count2 = 0
if 5 <= C <= 20 and 5 <= R <= 20:
    a = [[0] * C for _ in range(R)]
    col_check = [0 for _ in range(C)]  # col_check는 이전의 열에서 1이 나왔는지 확인용!
    for i in range(R):
        x = [int(x) for x in input().split()]
        for j in range(C):
            a[i][j] = x[j]

    for i in range(R):
        if sum(col_check) != C:  # 확인할 행이
            col = i
            count = 0
            row_check.clear()
            for j in range(C):
                if a[i][j] == 0 and col_check[j] == 0:
                    row_check.append(j)
                elif a[i][j] == 1:
                    col_check[j] = 1  # j열은 다음부터 확인 안한다는 뜻
            for k in range(C):
                if i < R - 1:
                    if a[i + 1][k] == 1:
                        col_check[k] = 1
        else:
            col = i - 1
            break
    if col >= 3:
        for i in (row_check):
            count2 = 0
            for j in range(col - 3, col + 1):
                count = 0
                for k in range(C):
                    if a[j][k] == 1:
                        count += 1
                if count == C - 1:
                    count2 += 1
            check.append(count2)
        for i in range(len(check)):
            if check[i] == max(check) and max(check) != 0:
                print(row_check[i] + 1, end=" ")
                print(check[i])
                break
            elif max(check) == 0:
                print(0, end=" ")
                print(0)
                break
    elif 0 <= col <= 2:
        print(0, end=" ")
        print(0)