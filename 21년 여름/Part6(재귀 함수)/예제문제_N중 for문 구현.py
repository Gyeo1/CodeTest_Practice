# template
global n
n = 3
Number = [0 for _ in range(n)]


def EqualCheck(a, b):  # 현재 값 a가 이전 값b와 같은지 확인
    count = 0
    for i in range(len(b)):
        if a == b[i]:
            return 0  # 같다 즉 포함하는게 있다면 return 0을 한다.
    return 1  # for문을 다돌아 즉 a의 값이 b행렬에 포함이 안되 있다면 1 return


def recursion(x, Num):  # x는 현재 n은 마지막 값
    global n
    if x >= n:
        print(Num)
    else:
        for i in range(1, n + 1):  # x 번째 숫자를 i로 만든다.
            if EqualCheck(i, Num):
                Num[x] = i
                recursion(x + 1, Num)  # 재귀 함수 시작
                Num[x] = 0  # 이후의 재귀함수가 끝나면 해당 부분을 0으로 만들어줌 (이후에 다른 값 넣기 위함)


recursion(0, Number)  # 0인 이유는 행렬의 인덱스가 0부터 시작하기 때문?