# def solution(numbers, target):
#     answer = 0
#     numbers.sort(reverse=True)
#     count = 0
#     def recursive(check,current,target):
#         nonlocal count
#         check[current] = -(check[current])
#         if sum(check)==target:
#             count+=1
#             return count
#         if sum(check)<target and current<len(check)-1:
#             check[current] = -(check[current])
#             current += 1    #다음 인덱스로?
#             recursive(check,current,target)
#         if sum(check)>target and current<len(check)-1:
#             current+=1
#             recursive(check,current,target)
#         return count
#     for i in range(len(numbers)):
#         check=numbers[:]
#         count=0
#         if sum(check)==target:
#             answer+=1
#             break
#         elif sum(check)<target:
#             break
#         answer+=recursive(check,i,target)
#     return answer
# def solution(numbers, target):
#     if numbers == []:
#         if target == 0:
#             return 1
#         else:
#             return 0
#     else:
#         return solution(numbers[1:], target+numbers[0]) + solution(numbers[1:], target-numbers[0])
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, level
    while queue:
        s, l = queue.popleft()
        print(queue)
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))

    return answer
numbers=[1,1,4,3,2]
print(numbers[-1])
target=3
print(solution(numbers,target))
#숫자를 적절히 더하고 빼서 타겟 넘버를 완성하세요
#역수로 뒤집고 일단 다 더해봐 더한 값이 target보다 작으면 return 0
#더한 값이 target보다 크면 number[0]부터 -로 바꿔주고 다시 실행해 본다.
