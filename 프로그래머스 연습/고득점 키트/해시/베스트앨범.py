#https://programmers.co.kr/learn/courses/30/lessons/42579 level3

#Question? 장르별로 가장 많이 재생된 노래를 두개씩 모아 앨범 출시하려함 수록기준은 다음과 같다
#1) 속하논래가 많이 재생된 장르부터 수록, 2)장르에서 많이 재생된 노래 수록 3)재생횟수가 같으면 고유번호가 낮은 노래 수록
#노래의 고유 번호를 순서대로 return하기

def solution(genres, plays):
    answer = []
    dic1=dict()      #재생횟수, 고유번호 저장용
    dic2=dict()      #총 재생횟수 저장용

    for i in range(len(genres)): #장르별 재생횟수, 고유변호 총 재생횟수 저장
        if genres[i] not in dic1.keys():
            dic1[genres[i]]=[(plays[i],i)] #
            dic2[genres[i]]=plays[i]
        else:
            dic1[genres[i]].append((plays[i],i))
            dic2[genres[i]]+=plays[i]

    for j in dic1.keys():       #dic1즉 장르별 재생횟수를 큰 순서대로 정렬, 재생수가 같으면 고유번호 순으로 정렬
        dic1[j].sort(key=lambda x:(x[0],-x[1]),reverse=True)
            #lambda x: (첫번째 조건, 두번째 조건이다)

    print(dic1)


    while dic1:
        check = dic2.items()        #dic2 즉 장르: 총 재생횟수를 받아서 최대값을 가지는 장르를 찾기
        for m in check:
            if max(dic2.values()) in m:
                for k in range(2):
                    answer.append(dic1[m[0]][k][1]) # 해당 장르와 관련된 고유 번호를 dic1에서찾는다
                    if len(dic1[m[0]])==1:
                        break
                del dic1[m[0]], dic2[m[0]]          # 다 추출한 장르는 지우기
                break

    return answer



geners=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 500, 500, 2500]
print(solution(geners,plays))