
#https://www.acmicpc.net/problem/5582 골드 5문제

string1=input()
string2=input()


def LCS(s1,s2): #Longest Common String의 개념임.
    max_val=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i==0 or j==0:
                continue
            if s1[i]==s2[j]:
                check[i][j]=check[i-1][j-1]+1
                max_val=max(max_val,check[i][j])
    print(max_val)

#LCS에서 맨 앞은 0으로 초기화 하기 때문에 빈칸 하나 추가
string1=" "+string1
string2=" "+string2
if len(string1)>len(string2):#긴 문자열을 기준으로 놓는다.
    check=[[0 for _ in range(len(string2))] for _ in range(len(string1))]
    LCS(string1,string2)
else:
    check = [[0 for _ in range(len(string1) )] for _ in range(len(string2) )]
    LCS(string2,string1)
# check=[[0 for _ in range(len(string1)+1)] for _ in range(len(string2)+1)]

# print(check)