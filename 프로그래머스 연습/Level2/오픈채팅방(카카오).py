def solution(record):
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
              "Change uid4567 Ryan"]
    uid_nickname = dict()  # 해시 자료형 특징: key가 최신값으로 업데이트 된다
    uid_list = []
    answer = []
    for i in range(len(record)):
        string = ""
        check = record[i].split() #핵심임 split으로 명령어 id nickname을 쪼개준다.
        if check[0] == "Enter":
            uid_nickname[check[1]] = check[2]
            uid_list.append(check[1])
            answer.append("님이 들어왔습니다.")
        elif check[0] == "Leave":
            uid_list.append(check[1])
            answer.append("님이 나갔습니다.")
        else:
            uid_nickname[check[1]] = check[2]
    for i in range(len(uid_list)):  # id 리스트를 가져와서 확인
        nickname = uid_nickname[uid_list[i]]
        if "들어왔습니다." in answer[i]:
            answer[i] = (nickname + answer[i])
        elif "나갔습니다." in answer[i]:
            answer[i] = (nickname + answer[i])
    return answer
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

#문제의 핵심은 split으로 공백끼리 분리하는것과 dict자료형으로 uid와 nickname간의 최신화
#그리고 마지막으로 uid만큼 새 리스트를 만들고 for문을 새 리스트 만큼 실행 시키는 것.