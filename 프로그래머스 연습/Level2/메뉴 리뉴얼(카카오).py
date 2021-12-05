from itertools import combinations
from collections import  Counter
def solution(orders, course):
    check_list = dict()
    answer = []

    def find_menu(orders, list1):

        nonlocal check_list
        for i in range(len(list1)):
            oreder_number = 0
            sort_list = "".join(sorted(list1[i]))

            if check_list.get(len(sort_list)) == None:
                check_list[len(sort_list)] = 0
            if check_list.get(sort_list) == None:
                for j in orders:
                    # print(j)
                    count = 0
                    for k in sort_list:
                        # print(k)
                        if k in j:
                            count += 1
                    if count == len(sort_list):
                        oreder_number += 1
                if (oreder_number) >= 2:
                    check_list[sort_list] = oreder_number
                if check_list[len(sort_list)] < oreder_number:
                    check_list[len(sort_list)] = oreder_number

    for string in orders:
        # string=list(string)
        # check = []
        for i in range(1, len(string)):
            if i + 1 in course:
                check = ((list(combinations(string, i + 1))))
                # print(check)
                find_menu(orders, check)
    for key, value in check_list.items():

        if str(type(key)) == "<class 'str'>" and check_list[key] == check_list[len(key)]:
            answer.append(key)
    answer = sorted(answer)
    return answer

'''
아래는 Counter활용한 방식, 코드 줄이기!!
from itertools import combinations
from collections import  Counter
def solution(orders, course):
    check_list = dict()
    answer = []

    for i in course:                                #1)코스 길이를 받아서
        check = []
        for string in orders:
            check += combinations(sorted(string),i) #2)주어진 문자열을 정렬하고 combination으로 코스 길이만큼의 조합을 생성!

        if len(check)>1:
            # print(check)
            most_use=Counter(check).most_common()   #3)Counter와 most_common을 활용,
                                                    #most_Common은 어떤 조합이 많이 사용됐는지를 보여준다
            answer+=[k for k, v in most_use if v>1 and v==most_use[0][1]] 
            #이거의 의미, most_use에서 k,v를 받아온다(2차원 배열이여야겠지?) 근데 v가 if문안의 값을 만족해야지 answer에 k가 들어간다!
            #4) most_use에서 1보다 크거 most_use[0][1]에 들어있는 가장 큰 값을 가지는 값들을 담는다
            answer=sorted(answer) #정렬한다

    return [''.join(v) for v in answer]             #5)'w' 'x' 를 묶기 위해서 
orders=["XYZ", "XWY", "WXA"]
course=[2,3,4]
print(solution(orders,course))
'''