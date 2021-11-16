def solution(numbers, hand):
    key_pad={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2],7:[2,0], 8:[2,1], 9:[2,2],
             "star":[3,0],0:[3,1],"sharp":[3,2]}
    left=key_pad["star"]
    right=key_pad["sharp"]
    answer = ''
    for i in numbers:
        if i==1 or i==4 or i==7:
            left=key_pad[i]
            answer = answer + "L"
        elif i==3 or i==6 or i== 9:
            right=key_pad[i]
            answer =answer+"R"
        elif i==2 or i==5 or i==8 or i==0:
            distance1=abs(key_pad[i][0]-left[0])+abs(key_pad[i][1]-left[1]) #키패드간 좌표거리
            distance2=abs(key_pad[i][0]-right[0])+abs(key_pad[i][1]-right[1])
            if distance1>distance2:
                right=key_pad[i]
                answer=answer+"R"
            elif distance1<distance2 :
                left = key_pad[i]
                answer = answer + "L"
            elif distance1==distance2:
                if hand=="right":
                    right=key_pad[i]
                    answer = answer + "R"
                else:
                    left = key_pad[i]
                    answer = answer + "L"

    return answer

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"
print(solution(numbers,hand))
# key_pad={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2],7:[2,0], 8:[2,1], 9:[2,2],
#              "star":[3,0],0:[3,1],"sharp":[3,2]}
# left=key_pad["star"]
# right=key_pad["sharp"]
# distance1=abs(key_pad[3][0]-left[0])+abs(key_pad[3][1]-left[1]) #키패드간 좌표거리
# print(distance1)
LRLLLRLLRRL