def solution(numbers):
    prev=[]
    for i in range(len(numbers)):
        prev.append(str(numbers[i]))

    prev.sort(key = lambda x: (x*4)[:4], reverse = True)

    if prev[0] != "0":
        answer = "".join(prev)
        return answer
    else:
        return "0"

numbers=[3, 30, 34, 5, 9,90,900,90]
# print(type(solution(numbers)),solution((numbers)))
print(solution(numbers))
'''
def solution(numbers):
    answer=''
    prev=[]
    for i in range(len(numbers)):
        prev.append(str(numbers[i]))

    prev.sort(key = lambda x: (x*4)[:4], reverse = True)

    if prev[0]=="0":
        return 0
    answer+="".join(prev)
    return answer'''