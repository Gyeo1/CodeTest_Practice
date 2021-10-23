N=int(input())
student_list=[]

def setting(array): #1번째 인덱스 값을 return
    return array[1]

for i in range(N):
    student_list.append(list((input().split())))

student_list=sorted(student_list, key=setting) #key를 인덱스 1번을 return으로 받아서 처리
#람다 기법은 다음과 같다
# student_list=sorted(student_list, key= lambda student:student[1])
for i in range(N):
    print(student_list[i][0],end=" ")