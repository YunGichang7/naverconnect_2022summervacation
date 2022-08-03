n = int(input("첫번째 수 입력: "))
m = int(input("두번째 수 입력: "))
def prime(n,m):
    numbers = [i for i in range(n, m+1)]
    count = 0
    for i in numbers:
        for j in range(2, i+1):
            if (j==i):
               count += 1
            elif (i % j ==0):
                break
    print("소수 개수:", count, "개")

prime(n,m)
