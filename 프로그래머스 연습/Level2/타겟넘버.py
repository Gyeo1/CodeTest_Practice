# def solution(numbers, target):
#     answer = 0
#     numbers.sort(reverse=True)
#     count=0
#
#     if sum(numbers)==target:
#         answer=1
#         return  answer
#     def recursive(current,index,target):
#         print(current)
#         count=0
#         if index >len(current)-1:
#             return count
#         if sum(current)==target:
#             count+=1
#             return count
#         elif sum(current)<target:
#             current[index] = (-current[index]) #현재 인덱스는 +로 바꿔주고 다음 인덱스를 -로
#             index += 1
#             if index < len(current) - 1:
#                 current[index] = (-current[index])
#                 count += recursive(current, index, target)
#         else: #current>target
#             index+=1
#             if index <= len(current) - 1:
#                 current[index]=(-current[index])
#                 count += recursive(current, index, target)
#
#         return count
#
#
#     for i in range(len(numbers)):
#         numbers[i] = (-numbers[i])
#         b=numbers[:]
#
#         if sum(numbers)>=target:
#             print(i,"번째 입니다")
#             answer+=recursive(b,i,target)
#             print(answer)
#         numbers[i] = (-numbers[i])
#
#     return answer
#
# test case 만 통과 ;
def solution(numbers, target):

    answer = 0
    N = len(numbers)

    def dfs(idx, numbers, total):
        nonlocal answer
        if (idx == N) and (total == target):
            answer += 1
            return
        if idx == N:
            return

        dfs(idx + 1, numbers, total + numbers[idx])
        dfs(idx + 1, numbers, total - numbers[idx])

    dfs(0, numbers, 0)

    return answer
numbers=[1, 1, 1, 1, 1]
target=5
print(solution(numbers,target))
#n개의 음이 아닌 정수가 있다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들어라
#sort 해주고