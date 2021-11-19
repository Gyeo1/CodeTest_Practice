def solution(N, stages): #N은 전체 스테이지 수, stages는 현재 도전자가 도전하고 있는 stage 를 뜻함. N+1이면 모두 클리어 했다
    #실패율 = 스테이지를 도달 했으나 클리어하지 못한 수/ 스테이지에 클리어 한 수
    answer = []
    check = [0] * (N+1)
    for i in stages:
        check[i-1]+=1
    check_sum=sum(check)
    for j in range(N+1):
        if check[j] !=0:
            check_sum-=check[j]
            check[j]=check[j]/(check_sum+check[j])
    check.pop() #계산 다 끝났으니 마지막꺼는 버림
    for k in range(N):
        max_index=check.index(max(check))
        answer.append(max_index+1)
        check[max_index]=-1
    return answer

N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
check = [0] * (N+1)
print(solution(N,stages))
