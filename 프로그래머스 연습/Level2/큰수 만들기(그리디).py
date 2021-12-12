def solution(number, k):
    results = []
    lenNumber = len(number)     #number의 전체 길이
    lenResult = lenNumber - k   #number-k 즉 결과값의 최대 길이
    th = -1
    for i in range(lenResult):  #결과값의 최대 길이만큼 반복
        val = "0"
        for j in range(th+1, lenNumber -(lenResult - len(results))+1):  #th부터 전체 길이-(결과로 나와야되는 길이-result 길이)

            if val < number[j]:     #val은 맨 처음에는 0, 이후에는 큰값이 들어간다
                th = j              #th에 인덱스 값 추가, 이후 인덱스 부터 실행한다.
                val = number[j]
                if val == "9": break
        results.append(val)        #result에 가장 큰 값을 넣어준다.
    answer = "".join(results)
    return answer