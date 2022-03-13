#https://programmers.co.kr/learn/courses/30/lessons/43164  레벨3

#Question ==>주어진 항공권으로 여행경로 짜려함, 항상 ICN 공항에서 출발한다. 방문하는 공항경로를 배열에 담아 retrurn
#모든 항공권을 사용해야된다.

def dfs(current,tickets):
    global answer
    if len(tickets)==1:
        answer.append(tickets[0][1])
        return
    check = []

    for i in range(len(tickets)):
        if tickets[i][0] == current:
            check.append((tickets[i][1],i))

    check.sort(key= lambda x:x[0])
    trig = 0
    print(current,check)
    print(tickets)
    for j in range(len(check)):
        if trig == 1:
            break
        for k in range(len(tickets)):
            if tickets[k][0] == check[j][0]:
                answer.append(check[j][0])
                del tickets[check[j][1]]
                trig = 1
                dfs(check[j][0], tickets)
                break

def solution(tickets):
    global answer
    answer = ["ICN"]
    check=[]
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            check.append((tickets[i][1],i))
    check.sort(key= lambda x:x[0])

    trig=0
    for j in range(len(check)):
        if trig==1:
            break
        for k in range(len(tickets)):
            if tickets[k][0] == check[j][0]:
                answer.append(check[j][0])
                del tickets[check[j][1]]
                trig=1
                dfs(check[j][0], tickets)
                break

    return answer

# tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]  #A-->B로 간다는 의미이다.
# tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets=[["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
tickets=[["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
# for i in tickets:
#     if "ICN" in i[0]:
#         print(i[1])
print(solution(tickets))