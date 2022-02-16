#https://programmers.co.kr/learn/courses/30/lessons/92342  2022카카오 블라인드

#k점을 더 많이 맞춘 사람이 해당 점수를 가져간다. 대신 동일 횟수로 맞추면 어피치에게 점수를 주는 패널티!
#추가 패널티는 점수가 같아도 어피치가 우승

max_val=0
abc=[]


def solution(n, info):
    global abc
    answer = [-1]

    for i in range(len(info)):
        check = [0 for _ in range(len(info))]
        for j in range(i, len(info)):
            if sum(check) + info[j] + 1 <= n:
                check[j] = info[j] + 1

            elif check_win(info, check):
                answer=check[:]

                check[j - 1] = 0
                if sum(check) + info[j] + 1 <= n:
                    check[j] = info[j] + 1
        # print(check)
    return answer

def check_win(l1,l2):
    global max_val,abc
    apeach = 0
    lion = 0
    for i in range(len(info)):
        if l1[i] < l2[i]:
            lion += (10 - i)
        elif l1[i] > l2[i]:
            apeach += (10 - i)

    if apeach < lion:
        if max_val < lion - apeach:  # 최대 점수차 갱신?
            max_val = lion - apeach
            return True
    #l1은 어피치 l2는 라이언 점수 값임
    return False



n=5
info=[2,1,1,1,0,0,0,0,0,0,0]	#10점부터 0점까지 맞춘횟수임.
print(solution(n,info))



#n은 화살의 갯수
#info는 어피치가 맞춘 과녁의 점수임


#가장 큰 점수를 먹는 것 부터 쭉 내려온다?
