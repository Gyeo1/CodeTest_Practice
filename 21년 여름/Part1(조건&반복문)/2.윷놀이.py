## template
#입력: 첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가 빈칸을 사이에 두고 주어진다.

a1, b1, c1, d1 = map(int, input().split())
a2, b2, c2, d2 = map(int, input().split())
a3, b3, c3, d3 = map(int, input().split())

first = a1 + b1 + c1 + d1
second = a2 + b2 + c2 + d2
third = a3 + b3 + c3 + d3
#출력:첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력 한다.
for i in (first, second, third):
    if i == 0:
        print("D")
    elif i == 1:
        print("C")
    elif i == 2:
        print("B")
    elif i == 3:
        print("A")
    else:
        print("E")