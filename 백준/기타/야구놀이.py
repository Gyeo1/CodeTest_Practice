## template
N = int(input())
strike = []
hun = []
ten = []
one = []
ball = []
count_s = 0
count_b = 0
count_ok = 0
result = 0
if 1 <= N <= 100:
    for i in range(N):
        n, s, b = map(int, input().split())
        # number.append([n//100,n%100//10,n%100%10])
        hun.append(n // 100)
        ten.append(n % 100 // 10)
        one.append(n % 100 % 10)
        strike.append(s)
        ball.append(b)
    print(hun)
    print(ten)
    print(one)
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and i != k and j != k:
                    count_ok = 0
                    for l in range(N):
                        count_s = 0
                        count_b = 0
                        if i == hun[l]:  # 백의 자리 i를 숫자와 비교
                            count_s += 1
                        elif i == ten[l]:
                            count_b += 1
                        elif i == one[l]:
                            count_b += 1

                        if j == ten[l]:  # 십의 자리 j를 비교
                            count_s += 1
                        elif j == hun[l]:
                            count_b += 1
                        elif j == one[l]:
                            count_b += 1

                        if k == one[l]:  # 일의 자리 k 비교
                            count_s += 1
                        elif k == ten[l]:
                            count_b += 1
                        elif k == hun[l]:
                            count_b += 1
                        if count_s == strike[l] and count_b == ball[l]:  # 스트라이크랑 볼 수가 같다?
                            count_ok += 1
                    if count_ok == N:
                        result += 1
    print(result)