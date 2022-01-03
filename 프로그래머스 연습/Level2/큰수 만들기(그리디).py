def solution(number, k):
    results = []
    lenNumber = len(number)     #number의 전체 길이
    lenResult = lenNumber - k   #number-k 즉 결과값의 최대 길이
    th = -1
    for i in range(lenResult):  #결과값의 최대 길이만큼 반복
        val = "0"
        #lenNumber-(lenResult-len(results))+1 여기 부분이 핵심, lenResult는 내가 구해야되는 숫자의 자릿수이고 result의 자릿수만큼 빼주는거다
        for j in range(th+1, lenNumber -(lenResult - len(results))+1):  #th부터 전체 길이-(결과로 나와야되는 길이-result 길이)

            print(j,end=" ")
            if val < number[j]:     #val은 맨 처음에는 0, 이후에는 큰값이 들어간다
                th = j              #th에 인덱스 값 추가, 이후 인덱스 부터 실행한다.
                val = number[j]
                if val == "9": break

        results.append(val)        #result에 가장 큰 값을 넣어준다.
        print(results,val, th)
    answer = "".join(results)
    return answer
number="4177252841"
k=4
print(solution(number,k))
