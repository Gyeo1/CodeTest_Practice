N=int(input())
chr_N=str(N)

for i in range(1,N+1):
    str_N=str(i)
    check=0
    for j in range(len(str_N)):
        check+=int(str_N[j])
    if check+i==N:
        trigger=1
        print(i)
        break
    if i==N:
        print(0)
        break