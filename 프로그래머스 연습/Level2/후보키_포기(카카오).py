# from itertools import combinations
# def solution(relation):
#     copy_list = relation[:]
#     unique_list = []
#     unique_idx = []
#     idx = 1
#     answer = 0
#     leng = len(copy_list[0])
#     def find_key(c_list, value):#후보키를 찾기 위한 과정
#         check = []
#         nonlocal unique_list
#         for i in range(len(c_list)):
#             check.append(list(combinations(c_list[i], value)))
#         # print(check)
#         for j in range(len(check[0])):
#             check_val = []
#             for k in range(0, len(check)):
#                 check_val.append(check[k][j])
#             if (len(list(set(check_val)))) == len(check_val):
#                 unique_list.append(check_val[0])
#     while idx <= leng:
#         unique_list = []
#         find_key(copy_list, idx)
#         print(unique_list)
#         # du_leng=len(unique_idx)
#         #아래 작업은 후보키를 제외시키기 위한 작업입니다.
#         for i in range(len(unique_list)):
#             index=""
#             for j in range(len(unique_list[i])):
#                 index= str(copy_list[0].index(unique_list[i][j])) #해당 값의 인덱스
#             unique_idx.append(index)
#             print(unique_idx)
#         idx += 1
#         leng = len(copy_list[0])
#     unique_list.clear()
#     # unique_list.append(unique_idx[0]) #unique_idx 첫번째 인자는 반드시 최소성, 유일성을 만족한다.
#     n=0
#     leng=len(unique_idx)
#     print(unique_idx)
#     while n<leng:
#         check = []
#         unique_list=[]
#         for i in range(len(unique_idx[n])):
#             check.append(unique_idx[n][i])
#
#         for j in range(n+1,len(unique_idx)):
#             count=0
#             for k in check:
#                 if k in unique_idx[j]:
#                     count+=1
#                     continue
#             if count==len(check) and j not in unique_list:
#                 unique_list.append(j)
#                 # del unique_idx[j]
#
#         for l in range(len(unique_list)):
#             del unique_idx[unique_list[l]-l]
#             print(unique_idx)
#         n+=1
#         leng = len(unique_idx)
#     unique_list.sort()
#     print(unique_idx)
#     return len(unique_idx)

from itertools import combinations
def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)
relation=[["a","1","aaa","c","ng"],
["a","1","bbb","e","g"],
["c","1","aaa","d","ng"],
["d","2","bbb","d","ng"]]
relation2=[['a',1,'aaa','c','ng'],
           ['b',1,'bbb','c','g'],
           ['c',1,'aaa','d','ng'],
           ['d',2,'bbb','d','ng']]
relation3=[["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"],
           ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]
# print(solution(relation))
# print(solution(relation2))
print(solution(relation3))
# print(list(combinations(relation[1],2)))
