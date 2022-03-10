# https://programmers.co.kr/learn/courses/30/lessons/42840 레벨 1

#수포자 3인방인 문제를 전부 찍으려 한다. 문제의 답이 answers로 주어졌을때 가장 많이 문제를 맞춘 사람은 누군지 return하시오

def solution(answers):
    people=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    check = [0 for _ in range(3)]
    answer=[]
    len_people=[len(people[0]),len(people[1]),len(people[2])]
    len_ans=len(answers)
    for i in range(len(answers)):
        for j in range(len(people)):
            if answers[i]==people[j][i%len_people[j]]: # 나머지 연산을 통해 사람의 패턴 길이의 반복대로
                check[j]+=1

    max_val=max(check)
    for i in range(len(check)):
        if check[i]==max_val:
            answer.append(i+1)

    return answer
answers=[1,2,3,4,5]
# answers=[1,3,2,4,2]
print(solution(answers))
