#문제: 체스판의 좌표정보가 있을때 나이트가 움직일 수 있는 거리의 수를 나타내시오
#A-H 1-8까지 있음
def solution(pos):
    answer = 0
    n_1=pos[0]
    n_2=int(pos[1])
    # A~H는 아스키 코드 값으로 65~72사이의 수이다.
    #그냥 8번 돌려서 확인하면 됨 대신 n_1의 값은 ord가 65<=ord<=72를 유지하도록!


    #좌로 2칸 이동 위아래
    if ord(n_1)-2 >= 65 and n_2+1 <= 8:
        answer+=1
    if ord(n_1) - 2 >= 65 and n_2 -1 >=1:
        answer += 1

    #오른쪽 2칸 이동후 위 아래
    if ord(n_1) +2 <=72 and n_2+1<=8:
        answer += 1
    if ord(n_1) +2 <=72 and n_2-1 >=1:
        answer += 1
    
    #위로 2칸 이동후 양옆 확인
    if n_2+2 <=8 and ord(n_1)+1<=72:
        answer += 1
    if n_2 + 2 <= 8 and ord(n_1) - 1 >=65:
        answer += 1

    #아래로 2칸 이동후 양옆 확인
    if n_2-2 >=1 and ord(n_1)+1 <= 72:
        answer += 1
    if n_2-2 >=1 and ord(n_1)-1 >= 65:
        answer += 1

    return answer

pos = "C3"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")