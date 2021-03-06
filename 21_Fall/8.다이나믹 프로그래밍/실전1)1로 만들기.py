# #정수 x가 주어질때 주어지는 4가지 방법으로 1을 만드는 최소 횟수를 출력하시오
# #우선순위?
#
# #노가다로 풀기
# #내 코드의 문제점=> Bottom-Up 방식으로 해야되는데 제일 큰수에서 작은수로 내려가는 방식을 채택함!
# X = int(input())
# count=0
# while 1:
#     if X==1:
#         break
#     if X%5==0:
#         X= X/5
#         count+=1
#     elif X%3==0:
#         if (X-1)%5==0:
#             X-=1
#             count+=1
#             continue
#         X=X/3
#         count+=1
#     elif X%2==0:
#         if (X-1)%5==0:
#             X-=1
#             count+=1
#             continue
#         elif (X-1)%3==0:
#             X-=1
#             count+=1
#             continue
#         X=X/2
#         count+=1
#     else:
#         X-=1
#         count+=1
# print(count)

# #정석 풀이인 보텀 업 방식을 사용해 보자.
#Bottom-Up: 1~input 까지에서
x=int(input())

d=[0]*30001                         #주어진 범위의 값만큼 초기화 해줘라

for i in range(2,x+1):
    d[i]=d[i-1]+1                   # 현재 인덱스에 이전 값의 처리한 값에 대해

    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)    #현재 수에서 1 뺏을 때 보다 //2를 한 값의 처리량이 작은가?
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)

print(d[x])


#순서를 생각해보자. i=2일때 d[2]=d[1]+1 이때 d[1]=0이므로 d[2]=1이다.
# 2는 2의 배수이므로 d[2]=min(1,1)이니깐 그냥 d[2]=1이됨

#3일경우 d[3]=d[2]+1 즉 1만 뺏을 경우에는 d[3]=2이다
#이때 3은 3의 배수이므로 d[3]=min(d[3], d[1]+1) 이때 d[3]=2이고 d[1]은0 즉 2,1중엔 1이 더 크므로 d[3]=1이된다.

#핵심은 이것 ==> 1)일단 -1을 햇을때 인덱스의 처리값을 가져와서 +1을 받아준다
#2)현재 인덱스가 2,3,5 로 나눠지는지 확인, 나눠지면 1)에서 나온 값과 나눠진 인덱스에서 나온 연산값+1을 한값중 작은값을 선택.