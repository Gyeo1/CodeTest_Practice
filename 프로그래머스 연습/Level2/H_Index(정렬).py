#어떤 과학자가 발표한 논문 n 편중 h번 이상 인용된 논문이h편 이상이고 나머지가 h 이하라면 h의 최대값이 H-Index다.
def solution(citations):
    check=[]
    citations.sort(reverse=True)#큰수부터 정렬
    if max(citations)==1 or max(citations)==0:
        answer=max(citations)
    else:
        for i in range(len(citations)):
            if citations[i]>=(i+1):#기준이 인덱스가 아니라 논문 번호 기준이다.
                check.append(i)
        answer=max(check)+1
    return answer

citations=[9, 7, 6, 2, 1]
print(solution(citations))
#H-index란 결국 큰수부터 나열하고 인덱스+1(논문 번호)값이 인용수보다 적어지는 부분을 찾는 거다.
#ex)9 7 6 2 1에서는 4번째 부터 2가 되므로 그 앞인 3이 최대 H가 된다.