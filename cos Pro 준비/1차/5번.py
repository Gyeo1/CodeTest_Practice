# def solution(n): #완전 잘못된 풀이이다.
#     answer = 0
#     check=[[0 for _ in range(n)] for _ in range(n)]
#     start=1
#     #소용돌이 만드는 for문 한마디로 0,2,4번째에서는 왼쪽에서 오른쪽 그 외는 오른쪽에서 왼쪽(역순)으로 오는것을 활용하여 값을 넣어줌
#     for i in range(n):
#         if i ==0 or i%2==0: #정순으로 시작
#             for j in range(n):
#                 check[i][j]=start
#                 start+=1
#         else:
#             for j in range(n-1,-1,-1): #역순으로 시작
#                 check[i][j] = start
#                 start += 1
#
#     #만들어진 check의 대각선의 숫자를 가져온다.
#     idx=0
#     for k in range(n):
#         # print(check[k])
#         answer+=check[k][idx]
#         idx+=1
#     return answer


#소용돌이 수의 핵심은 바로 일정한 반복성임
# n=4일때 1 2 3 4 -> 5 6 7-> 8 9 10 -> 11 12 -> 13 14-> 15 ->16
#뭐가 보이나? n=4즉 n번 연속(반복)되는 경우는 1번이고 n-1번 부터 1까지는 2번씩 반속 된다
#4 ->3->3->2->2->1->1 이렇게 참고로 이렇게 반복되는 총 횟수는 n*2-1이다 ex)n=5면 5 4 4 3 3 2 2 1 1 즉 9번반복해야 다 채워진다.
#그리고 그럴때 방향성의 규칙은 row=0 col=1/row=1 col=0/ row=0 col= -1/ row=-1 col=0이 반복됨
#
def solution(n):
    answer=0
    start=0
    while start< n*n:
        start+=1
        print(start,end=" ")
    print("final_num",start )
    return answer
n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")