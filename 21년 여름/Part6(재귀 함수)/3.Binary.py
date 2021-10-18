## template
#2진수란 2**step에서 몫이 1이상이고 number에서 2**step을 뺀 값이 2**(step+1) 값에 의해 나머지가 0이면 1, 아니면 0 이다.
global result,check
number=int(input())
result=[]
def binary(maximum,number,step):
  global result,check
  if (2**step)>maximum:
    result.reverse()
    s="".join(result)
    print(s)
  else:
    if number//(2**step)>=1: # 현재 단계에서(2의 step제곱) 몫이 1이상이고
      check=number -2**step
      if check%(2**(step+1)) ==0: #number와 몫을 뺀값이 다음 제곱근에 나눠지면(나머지0) 1이다
        result.append('1')
        number=number -(2**step) #number는 빼준다 다음 연산에서 쓰기 위해
      else:
        result.append('0')
      binary(maximum,number,step+1)
if 0<=number<=1000:
  binary(number,number,0)