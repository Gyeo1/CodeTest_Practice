# https://www.acmicpc.net/problem/2579      실버 3문제

#계단을 오르는 규칙 1. 계단은 한번에 한계단 or 두 계단씩 오를 수 있다.
#2.연속된 세 개의 계단을 모두 밟아서는 안된다. 단 시작점은 계단 x
#3. 마지막 도착 계단은 반드시 밟아야 한다. ==> 뒤에서 부터 시작해야되나?


def solution(stair):
    if N == 1:
        print(stair[0])
        return
    if N == 2:
        print(stair[0]+stair[1])
        return
    check = [stair[0]]
    check.append(max(stair[0] + stair[1], stair[1]))  # 햇갈린 부분, 뒤에서 시작해도
    check.append(max(stair[0] + stair[2], stair[1] + stair[2]))
    for i in range(3, N):
        check.append(max(check[i - 2] + stair[i], check[i - 3] + stair[i - 1] + stair[i]))
    print(check[-1])
    return

N=int(input())

stair=[]
for _ in range(N):
    stair.append(int(input()))

solution(stair)
