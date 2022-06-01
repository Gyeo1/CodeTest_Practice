def func_a(times):
    hour = int(times[:2])
    minute = int(times[3:])
    return hour * 60 + minute


def solution(subway_times, current_time):
    current_minute = func_a(current_time)  #빈칸 1: 현재 시간을 minute 방식으로 바꾸기 위한 함수 a에 넣는다.
    INF = 1000000000
    answer = INF
    for s in subway_times:
        subway_minute = func_a(s) #빈칸 2: subway_times에 있는 시간을 s에 넣는것 이므로 s를 넣어줌
        if subway_minute >= current_minute: #빈칸 3: 만약 열차 시간이 현재 시간 보다 크거나 같으면 남은 시간을 구함
            answer = subway_minute - current_minute#기본적으로 열차 시간은 오름차순으로 정렬되어 있어서 answer를 구하고 break를 건다
            break
    if answer == INF:
        return -1
    return answer


##
subway_times1 = ["05:31", "11:59", "13:30", "23:32"]
current_time1 = "12:00"
ret1 = solution(subway_times1, current_time1)

print("solution 함수의 반환 값은", ret1, "입니다.")

subway_times2 = ["14:31", "15:31"]
current_time2 = "15:31"
ret2 = solution(subway_times2, current_time2)

print("solution 함수의 반환 값은", ret2, "입니다.")
