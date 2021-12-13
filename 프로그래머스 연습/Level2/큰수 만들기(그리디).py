def solution(number, k):
    results = []
    lenNumber = len(number)     #number의 전체 길이
    lenResult = lenNumber - k   #number-k 즉 결과값의 최대 길이
    th = -1
    for i in range(lenResult):  #결과값의 최대 길이만큼 반복
        val = "0"
        print(lenNumber -(lenResult - len(results))+1)
        for j in range(th+1, lenNumber -(lenResult - len(results))+1):
            #th부터 전체 길이-(결과로 나와야되는 길이-result 길이)
            #lenNumber -(lenResult - len(results))+1 ==>이게 길이를 보장한다
            #ex)예제에서 k=4일때 최대길이는 6이다 이를 number의 길이-6을 해주면 뒤에는 무조건 6자리가 남기 때문에 가능
            #추후에 result 값이 추가되면 6->7->8->9 이렇게 한칸씩이동하면서 뒤에 길이를 보장한다.
            if val < number[j]:     #val은 맨 처음에는 0, 이후에는 큰값이 들어간다
                th = j              #th에 인덱스 값 추가, 이후 인덱스 부터 실행한다.
                val = number[j]
                if val == "9": break
        results.append(val)        #result에 가장 큰 값을 넣어준다.
    answer = "".join(results)
    return answer

number="4177252841"
k=4
print(solution(number,k))