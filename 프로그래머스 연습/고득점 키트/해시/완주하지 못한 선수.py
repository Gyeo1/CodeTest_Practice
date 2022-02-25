#https://programmers.co.kr/learn/courses/30/lessons/42576 level1

#문제 풀이 접근 -->참여자의 정보를 dict 자료형으로 저장, 이때 값은 1을 넣어줌
#만약 동명이인이 참가했다면 dict[참가자]의 값을 +1 시켜준다
#두번째 for문에서는 완주자의 정보를 받고 dic[이름]의 값을 -1 해주고 dic값이 0이면 해당 key를 지운다
#그렇게 해서 남아 있는것이 완주하지 못한 사람이다.

def solution(participant, completion):

    dic=dict()
    for i in participant:
        if i not in dic.keys():
            dic[i]=1
        else:
            dic[i]+=1
    for j in completion:
        dic[j]-=1
        if dic[j] ==0:
            del dic[j]
    answer=list(dic.keys())[0]
    print(answer)
    return answer

# participant=["mislav", "stanko", "mislav", "ana"] #참여자
# competion=["stanko", "ana", "mislav"]   #완주자
participant=["leo", "kiki", "eden"]
competion=["eden", "kiki"]
solution(participant,competion)
#Question==>완주하지 못한 선수의 이름을 return하세요