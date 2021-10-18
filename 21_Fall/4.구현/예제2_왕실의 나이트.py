import time
#이동 가능한 경우= 수평 2칸으로 이동후 수직 1칸 or 수직 2칸 이동후 수평 1칸
#a는 아스키코드로 97/ h는 104다

#나의 풀이
# place=input()
# count=0
# for i in range(1): #이동 가능한 방법은 최대 4개이니깐
#     if int(place[1])+2<=8  :
#         if ord(place[0])+1<=104:
#              count+=1
#         if ord(place[0])-1>=97:
#             count+=1
#     if int(place[1])-2>=1:
#         if ord(place[0])+1<=104:
#              count+=1
#         if ord(place[0])-1>=97:
#             count+=1
#     if ord(place[0])+2 <=104:
#         if int(place[1])+1<=8:
#             count+=1
#         if int(place[1])-1>=1:
#             count+=1
#     if ord(place[0])-2 >=97:
#         if int(place[1])+1<=8:
#             count+=1
#         if int(place[1])-1>=1:
#             count+=1
#
# print(count)
#
# start_time = time.time()# 측정 시간
# end_time=time.time()# 측정 종료
# print("걸린시간은 ?:", end_time-start_time);

#좌표 형식으로(정석 풀이)
#생각해 둘것 1) 좌표형식의 문제(이동과 관련된)는 항상 이동 관련 명령을 배열로 만들기
#2) for문에는 range 뿐만 아니라 배열을 한개씩 받아 올 수 있다.

place=input()
row=int(place[1])
col=int(ord(place[0])) #a는 97이다.
count=0
step=[(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2)] #나이트가 이동할수 있는 경로 2개!
for i in step: #이렇게 step으로 받아오면 (-2,1)을 한번씩 받아올 수 있다.
    next_row=row+i[0]
    next_col=col+i[1]
    if next_row>=1 and next_row<=8 and next_col>=97 and next_col<=104:
        count+=1
print(count)