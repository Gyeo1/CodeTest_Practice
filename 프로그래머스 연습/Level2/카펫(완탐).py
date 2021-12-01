#중앙은 노란색, 테두리는 갈색, 격자수가 주어지고 카펫의 가로 세로 크기를 구해라
def solution(brown, yellow):
    n=2  #가로길이
    answer = []
    if yellow==1:
        answer=[3,3]
    else:
        while 1: #여기서 brown 갯수도 파악해줘야된다.
            if yellow%n==0: # 2
                if (n+2)*2+int(yellow/n)*2 ==brown:
                    answer.append(n + 2)
                    answer.append(int(yellow/n)+2)
                    break

            n+=1#여기가 문제였다. 1개씩 추가 해줘도 전부다 확인이 가능!
            #not n+=2
    if answer[0]<answer[1]:
        answer[0],answer[1]=answer[1], answer[0]

    return answer

brown=36
yellow=64
print(solution(brown,yellow))