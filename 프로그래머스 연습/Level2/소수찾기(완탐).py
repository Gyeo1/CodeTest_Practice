import math,itertools

def solution(numbers):
    numbers_list = []
    set_list = []
    check = []
    answer = 0
    def is_prime_number(number): #소수 판별 함수
        nonlocal answer
        for i in range(2, int(math.floor(math.sqrt(number)+1))): #약수의 법칙
            if number % i == 0:
                return
        answer += 1
        print(number)
        return
    for i in numbers:
        numbers_list.append(i)
    for j in range(1, len(numbers_list) + 1):#순열로 가능한 문자 조합을 넣는다.
        #for문의 이유? ==> 순열의 묶는 단위를 늘려주는거다, 1개로 표현가능한 순열~최대로 표현 가능한 순열
        b = list(map("".join, itertools.permutations(numbers_list, j)))
        set_list.append(list(set(b))) #set으로 중복되는 값 삭제(+list화)
    for k in range(len(set_list)):
        for l in range(len(set_list[k])):
            if int(set_list[k][l]) >= 2:
                check.append(int(set_list[k][l]))#모든 순열을 하나의 리스트로 통합.
    check=list(set(check))
    for l in check:
        is_prime_number(int(l))
    return answer

#주어진 문자열로 소수 몇개를 만드는지 찾기, 소수? ==> 자기 자신과 1만 약수로 가지는 수.
#소수는 간단하게 약수의 법칙으로 구하자
#약수의 법칙: 약수는 중간 기준으로 대칭이된다 ==>중간 값 기준으로 for 문 돌려서 0이 나오면 소수가 아님
numbers="101010"
print(solution(numbers))
