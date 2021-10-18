## template
#문제 N,K에서 N의 약수중 K번째 큰 약수 출력.
N, K = map(int, input().split())
count = 0
if 1 <= N <= 10000 and 1 <= K <= N:
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
        if count == K:#K번째 찾으면 for문 탈출.
            print(i)
            break
    if count < K:#만약 약수 숫자가 K보다 작으면 0 출력
        print(0)