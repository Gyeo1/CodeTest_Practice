import sys
# input=sys.stdin.readline

string_S=(input())
string_P=(input())
len_P=len(string_P)
print(len_P)
table=[0]*len_P
check_len=0
# print(string_P[len_P-1:])
for i in range(1,len(string_P)):
    prefix=string_P[:i]
    # print(prefix,end="다음 ")
    for j in range(i,len_P):
        suffix=string_P[len_P-j:len_P-j+i]#핵심
        # print(suffix,end=" ")
        if prefix==suffix:
            table[i]=j
    print()
print(table)
# print(string_P,len_P)
# print(check)
# point=len_P-check[2]
# #len_P-j가 다음 시작 지점
# start=0
# # print(s)
# for _ in range(7):
#     if string_S[start:start+len_P] == string_P:
#         print(1)
#         break
#     print(start,string_S[start:start+len_P],string_P)
#     start+=(point)
#     # print(start,len_P)
# print(2)
