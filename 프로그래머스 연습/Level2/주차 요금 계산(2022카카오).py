#https://programmers.co.kr/learn/courses/30/lessons/92341      카카오 문제
import math
def solution(fees, records):
    answer = []
    dic1=dict()

    # record에 있는 정보를 dict자료형에 정리하기 위한 작업
    for i in records:
        check= i.split()                    #split으로 시간정보, 차량 정보를 분리한다.
        if check[1] not in dic1.keys():
            dic1[check[1]]=[check[0]]       #차량장보를 key값, 시간정보를 value 값으로 저장
            continue
        dic1[check[1]].append(check[0])

    #
    for j in sorted(dic1.keys()):           #작은 차량 번호 대로 가져온다.
        time=0
        if len(dic1[j])%2!=0:               #만약 정보가 홀수? ==>마지막에 나가지 않음 23:59 추가
            dic1[j].append('23:59')

        for k in range(0,len(dic1[j]),2):   #2개씩 처리할꺼니 맨뒤에 2
            in_time=dic1[j][k]              #dic1에 저장된 ㅅ
            out_time=dic1[j][k+1]
            hour=int(out_time[:2])-int(in_time[:2])
            min=int(out_time[3:])-int(in_time[3:])
            time+=(hour*60+min)
        if time<=fees[0]:
            answer.append(fees[1])
            continue
        answer.append(fees[1]+(math.ceil((time-fees[0])/fees[2]))*fees[3])

    print(answer)

    return answer



fees=[180, 5000, 10, 600]    #기본 시간, 기본요금, 단위 시간, 단위 요금
records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees,records)
#비용 계산법 5000+[(총 시간 - 기본시간)/단위 시간]*단위 요금이다  이때 []값은 올림을 해준다 걍 int 붙이면됨
#만약 OUT이 없다면 23:59에 나간것으로 생각
#출력은 차량 번호가 작은 순서대로
# i=(1/60)
# print(i.__ceil__())