import re
def solution(s):
    answer = []
    check = []
    s = re.split(r'},', s)  #정규 표현식으로 쪼개준다. {숫자들},{숫자들} 이런 구조로 되어 있으므로 },로 짜르면 된다.
    for i in range(len(s)):
        check.append(re.findall(r'\d+', s[i])) #\d로 숫자들만 뽑아낸다. 이때 \d+를 해줘야 1111,112 이런 값들도 다 받는다.
    check.sort(key=lambda x: len(x))            #lamda로 x의 길이가 가장 작은 수부터 나열
    for j in range(len(check)):
        for k in range(len(check[j])):
            if int(check[j][k]) not in answer:  #for문을 돌면서 중복되지 않는 값들만 담는다.
                answer.append(int(check[j][k]))
    return answer

s="{{20,111},{111}}"
solution(s)