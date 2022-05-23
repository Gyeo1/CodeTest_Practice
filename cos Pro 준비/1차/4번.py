#코드 작성 문제
def solution(num):
    # 주어진 num에 +1한 값을 0이 없는 숫자체계로 표현해라
    #간단하게 +1해주고 0인걸 1로 바꾸기만 하면됨
    answer = ""
    num = num + 1
    check=[]
    for i in range(len(str(num))):
        check.append(int(str(num)[i]))
    for j in range(len(check)):
        if check[j] == 0:
            check[j]=1
        answer+=str(check[j])
    return int(answer)


num = 9949999
ret = solution(num)

print("solution 함수의 반환 값은", ret, "입니다.")
