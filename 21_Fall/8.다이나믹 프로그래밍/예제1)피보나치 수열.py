#다이나믹 프로그래밍? ==>중복되는 연산을 줄인다

#피보나치 수열 ==> 이전 두항의 합을 현재 항으로 설정하는 수열

#fibo1 처럼하면 x값이 커지면 연산이 기하급수적으로 늘어난다!
def fibo1(x):
    if x==1 or x==2:
        return 1
    return fibo1(x-1)+fibo1(x-2)    #==>동일한 함수가 겹쳐서 호출될 가능성을 제공한다.



#2번째 방식 Top-Down 방식==>큰문제를 해결하기 위한 작은 문제 호출
d=[0]*200            #meoization기법을 사용한다
#메모제이션 기법? ==> Dynamic 프로그래밍을 구현하는 방법중 하나로 한번 구한 결과를 메로리 공간에 저장, 다시 호출 안되게 한다! (캐싱?)

def fibo2(x):
    print('f('+str(x)+')',end=" ")
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]             #핵심 ==>d[x]가 0이 아니면 이미 한번 사용된거다 ==>바로 그냥 호출한다
    d[x]=fibo2(x-1) +fibo2(x-2)
    return d[x]


#3번째 방식 Bottom-Up 방식 ==>작은 문제 부터 차근차근 답을 도출!
d1=[0]*100
d1[1]=1
d1[2]=1
n=10
for i in range(3,n+1):
    d1[i]=d1[i-1]+d1[i-2]
print(d1[n])