#https://programmers.co.kr/learn/courses/30/lessons/92335        2022 KAKAO BLIND RECRUITMENT 문제

#양수 n이 주어질때 k진수로 바꾸고 조건에 맞는 소수의 개수 찾기
def IsPrime(n):
    for i in range(2,int(n**(0.5))+1 ):
        if n%i==0:
            return False #소수가 아니면 False
    return True

def solution(n, k):
    answer=0
    #k진수로 바꿔주는 과정임
    if k!=10:
        check = n // k
        translate_k = ""
        translate_k = str(n % k) + translate_k
        while check > 0:
            translate_k = str(check % k) + translate_k
            check = check // k
    else:       #10진수면 걍 입력 받은 그대로임
        translate_k=str(n)

    #k진수로 변환된 수에서 조건에 맞는 소수를 찾기     *핵심은 자리수에 0이 없다!

    check=""

    for i in range(len(translate_k)):

        if (translate_k[i] =='0'):          #i=0즉 traslate_k에서 0을 만나면 이전 값들로 소수 판단
            if check=="1" or check=="":
                check = ""
                continue
            if IsPrime(int(check)):
                answer+=1

            check=""
            continue
        check += translate_k[i]

    if check !="1" and check!="" and (IsPrime(int(check))): #마지막 경우의 수인 P만 있는 경우와 0P를 위한 걸 한번더 실행
        answer+=1
    #에리토네스 체 생성
    # array=[True]*(translate_k+1)          #메모리 에러뜸;
    # for i in range(2, translate_k+1):
    #     if array[i]==True:
    #         j=2
    #         while i*j<=translate_k:
    #             array[i*j]=True
    #             j+=1
    # print(array)

    return answer

#일단 주어진 n은 k 진수로 바꿔야지
n=1
k=4
print(solution(n,k))