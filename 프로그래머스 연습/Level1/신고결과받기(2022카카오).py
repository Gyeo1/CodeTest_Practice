# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3 , 카카오 2022 블라인드 Recruitment

def solution(id_list, report, k):
    dic1 = dict() #key: 신고자  value: 신고 한 사람
    dic2=dict() #key: 신고 당한 사람,  value: 신고당한 횟수
    for i in id_list:
        if i not in dic1.keys():
            dic1[i] = set()
            dic2[i]=0
    #신고자가 누굴 신고했는지 dic1에 정리
    for i in report:
        check = i.split()
        dic1[check[0]].add(check[1])
    print(dic1)
    # print(dic1.values())

    #신고된 횟수를 측정
    banned=[]                   #벤 리스트임
    for reported in dic1.values():
        for person in reported:
            dic2[person]+=1
            if dic2[person]==k: #만약 person즉 신고된 사람이 k번 신고됐다면
                banned.append(person)#ban 리스트에 올린다
    print(dic2)
    print(banned)


    answer = [0 for _ in range(len(id_list))]
    number = 0
    for j in dic1.values():

        for k in banned:
            if k in j:
                answer[number]+=1
        number+=1

    return answer
#한번에 한명의 유저 신고, 신고 횟수에 제한은 없지만 동일 유저에 대한 횟수는 1회로 처리 ==k번 이상 신고된 유저는 게시판 정지
#정지된 유저에 대해 신고한 유저는 메일로 발송, 마지막에 한번에 정리 다 때리는 형식이다.
#result로 정지된 유저의 수를 받게 된다.

id_list=["muzi", "frodo", "apeach", "neo"]
# id_list=["con", "ryan"]

# print(dic)
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# report=["ryan con", "ryan con", "ryan con", "ryan con"]
#muzi frodo 면 muzi가 frodo를 신고했다란 의미

k=2 #k번 이상 신고 당하면 이용 정지


solution(id_list,report,k)
