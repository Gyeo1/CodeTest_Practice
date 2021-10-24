import sys

input_data=sys.stdin.readline().rstrip()
N,K= map(int,sys.stdin.readline().rstrip().split()) #
a=[]
for i in range(N):
    a.append(list(map(int,sys.stdin.readline().rstrip().split())))
print(input_data)
print(type(N),N,K )
print(a)