#K번의 바꿔치기를 해서 가장 큰 합을 가지는 배열 A 만들기
#A의 제일 작은 수와 B의 제일 큰수를 바꿔준다!
N,K =map(int,input().split())
A=(list(map(int,input().split())))
B=(list(map(int,input().split())))

A.sort()
B.sort()
if 1<=N<=100000 and 0<=K<=N and len(A)==N and len(B)==N: #수식이 실행되는 조건
    for i in range(K):
        if A[i]<=B[len(B)-1-i]:
            A[i],B[len(B)-1-i]= B[len(B)-1-i],A[i]
        else:
            break
    print(sum(A))
else:
    print("입력 값이 잘못되었습니다.")

