## template
R, C = map(int, input().split())  # C는 행 R은 열
K = int(input())
tirgger = 0  # 방향을 나타낸다 0(위),1(오른쪽),2(아래),3(왼쪽)
i = C - 1
j = 0
count = 0
x = 1
y = 0
if 5 <= R <= 1000 and 5 <= C <= 1000 and 1 <= K <= 100000000:
    a = [[0] * R for _ in range(C)]
    while (1):
        if K > (C * R):
            print(0)
            break
        if tirgger == 0:
            a[i][j] = 1
            count += 1
            i -= 1
            y += 1
            if count == K:
                print(x, end=" ")
                print(y)
                break
            if a[i][j] != 0 or i < 0:
                i += 1
                j += 1
                tirgger = 1
        elif tirgger == 1:

            a[i][j] = 1
            j += 1
            x += 1
            count += 1
            if count == K:
                print(x, end=" ")
                print(y)
                break
            if j == R or a[i][j] != 0:
                j -= 1
                i += 1
                tirgger = 2
        elif tirgger == 2:
            a[i][j] = 1
            y -= 1
            count += 1
            i += 1
            if count == K:
                print(x, end=" ")
                print(y)
                break
            if i == C or a[i][j] != 0:
                j -= 1
                i -= 1
                tirgger = 3
        elif tirgger == 3:
            a[i][j] = 1
            x -= 1
            count += 1
            j -= 1
            if count == K:
                print(x, end=" ")
                print(y)
                break
            if a[i][j] != 0 or i == C:
                j += 1
                i -= 1
                tirgger = 0
