def dfs(n, info, k, apeach, lion, temp):
    if n == 0: #남은 화살 숫자가 0이면 라이온과 어피치의 점수를 비교해 본다.
        global max_val, answer

        if lion - apeach > max_val: #점수차가 max_val보다 크면 answer에 정답 갱신
            max_val = lion - apeach
            answer = temp[:]

        elif lion - apeach == max_val and max_val != 0: #점수차가 max_val이랑 같으면서 max_val이 0이 아니면
            for i in range(10, -1, -1):
                if temp[i] > answer[i]:
                    answer = temp[:]
                    break
                elif temp[i] < answer[i]:
                    break
        return

    for i in range(k, 11):

        if n > info[i]:                         #남은 화살 수가 현재 apaech의 점수를 이길 수 있을 정도면?
            temp[i] = info[i] + 1               #temp에 값을 넣어줌
            if info[i] > 0:
                dfs(n - temp[i], info, i + 1, apeach - (10 - i), lion + (10 - i), temp) #만약 info가 0이 아니면 어피치의 점수가 빠지는 것이다.
                                            #dfs는 남은화살수, 어피치 정보, 확인 지점(k==i+1), 어피치 점수, 라이언 점수, 라이언 화살 정보
            else:
                dfs(n - temp[i], info, i + 1, apeach, lion + (10 - i), temp)    #info가 0 이면 어피치에선 빠지는 점수는 없다

            temp[i] = 0                         #다시 0으로 초기화

        else:                                   #어피치를 이기기 위한 화살 수가 부족하면 다음으로 넘기기

            if i == 10 :                    #만약 i==0이면 끝이므로 dfs0을 실시 0은 점수 확인이다.
                temp[i] = n
                dfs(0, info, i + 1, apeach, lion, temp)
                temp[i] = 0
            else:#남은 화살수를 그대로 주고 i+1시킨 값을 보낸다.
                dfs(n, info, i + 1, apeach, lion, temp)


def solution(n, info):
    global max_val, answer
    apeach = 0
    answer = [0] * 11
    max_val = 0

    for i in range(11):
        if info[i] > 0:  #어피치의 총 점수를 구한다
            apeach += 10 - i
    dfs(n, info, 0, apeach, 0, [0] * 11)    #dfs에 남은 화살 수와, 어피치의 정보 , 0 ,어피치의 점수, 라이언의 점수,등을 넣어보냄
    if answer == [0] * 11:
        answer = [-1]
    return answer

n=5
info=[2,1,1,1,0,0,0,0,0,0,0]
print(solution(n,info))