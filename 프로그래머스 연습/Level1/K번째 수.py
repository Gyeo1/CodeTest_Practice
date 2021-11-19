def solution(array, commands):
    check=[]
    answer = []
    for i in range(len(commands)):
        check=array[commands[i][0]-1:commands[i][1]]
        check.sort()
        answer.append(check[commands[i][2]-1])
    return answer

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]] #실질적으로 2는 인덱스1이다

print(solution(array,commands))#2 3 5 6