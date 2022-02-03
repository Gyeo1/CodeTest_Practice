#문자열을 리스트 형식으로 받고 뒤집어서 반환

list_1=["h","e","l","l","o"]
list_2=["h","a","b","a","n","a"]

#첫번째 방법 ==> reverse함수를 사용하기
list_1.reverse()
print(list_1)

#두번째 방법 two pointer로 서로 다른 값을
left=0
rigth=len(list_2)-1
while left<rigth:
    list_2[left],list_2[rigth]=list_2[rigth],list_2[left] #파이썬에서 제공하는 투 포인터 방식
    #파이썬의 특징 이렇게 순서를 바꾸는 것이 가능함.
    left+=1
    rigth-=1
print(list_2)