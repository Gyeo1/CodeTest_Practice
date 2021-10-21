# a=10
# def recursive_function(value):
#     if value!=0:
#         print("재귀 함수를 호출합니다",value)
#         value-=1
#         recursive_function(value)
#
# recursive_function(a) #이런 느낌으로 자기를 계속 호출할 수 있다.

#Factorial 예제
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n - 1)

    #n!=> n*n-1* ... 1
a=factorial_recursive(5)
print(a)