# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def func(record):  # func은 record의 값이 지는 경우를 알려줌
    if record == 0:  # record가 가위면 1즉 바위를 낸사람에게는 진다를 나타냄
        return 1
    elif record == 1:  # 바위는 보
        return 2
    return 0  # 보는 바위


def solution(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)):
        if recordA[i] == recordB[i]:
            continue
        elif recordA[i] == func(recordB[i]): #recordB[i]가 0고 recordA[i]=1이면 3점을 먹는 구조
            cnt = cnt + 3
        else:
            if cnt > 0: #한줄 추가한 부분. 해당문제의 문제점은 바로 맨 처음에서 질 경우 -1를 한다는 점임
                cnt = cnt - 1


recordA = [2, 0, 0, 0, 0, 0, 1, 1, 0, 0]
recordB = [0, 0, 0, 0, 2, 2, 0, 2, 2, 2]
ret = solution(recordA, recordB)

print("solution 함수의 반환 값은", ret, "입니다.")
