#https://www.acmicpc.net/problem/9012 백준 9012번

test_case=int(input())

def Is_VPS(value):
    if len(value)%2!=0:
        print("NO")
        return
    check=value.count("(")
    print(len(value),check)
    # return
for _ in range(test_case):
    string=input()
    Is_VPS(string)