## template
N = int(input())
X, Y, R = map(int, input().split())
if 6 <= N <= 100 and N % 2 == 0 and 1 <= X <= N and 1 <= Y <= N and 1 <= R <= N / 2:
    a = [[0] * N for _ in range(N)]  # N*N의 행렬 생성
    a[X - 1][Y - 1] = 'x'  # X는 행 Y는 열
    for i in range(1, R + 1):
        if Y - 1 + i < N:
            a[X - 1][Y - 1 + i] = i
        if Y - 1 - i >= 0:
            a[X - 1][Y - 1 - i] = i
        if X - 1 + i < N:  # 아래로
            a[X - 1 + i][Y - 1] = i
            for j in range(1, R + 1):
                if Y - 1 + j < N:
                    if i + j <= R:
                        a[X - 1 + i][Y - 1 + j] = i + j

                if Y - 1 - j >= 0:
                    if i + j <= R:
                        a[X - 1 + i][Y - 1 - j] = i + j

        if X - 1 - i >= 0:
            a[X - 1 - i][Y - 1] = i
            for j in range(1, R + 1):
                if Y - 1 + j < N:
                    if i + j <= R:
                        a[X - 1 - i][Y - 1 + j] = i + j

                if Y - 1 - j >= 0:
                    if i + j <= R:
                        a[X - 1 - i][Y - 1 - j] = i + j

    for i in range(N):
        for j in range(N):
            print(a[i][j], end=" ")
        print("")
