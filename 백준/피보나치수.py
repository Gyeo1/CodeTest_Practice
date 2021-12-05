value= int(input())
a_0=0
a_1=1
def fibo(value,a1,a2):
    a = a1 + a2
    if value==0:
        return a
    return fibo(value-1,a2,a)
if value>=2:
    print(fibo(value-2,a_0,a_1))
elif value==0:
    print(a_0)
elif value==1:
    print(a_1)