n = int(input("첫번째 수 입력: "))
m = int(input("두번째 수 입력: "))
numbers = [i for i in range(n, m+1)]

def printEven(numbers):
    for x in numbers:
        if x % 2 == 0:
            print(x)

def printmedium(numbers):
    medium = int((n+m)/2)
    if medium % 2 == 0:
        print(medium)
    else:
        print("중앙값이 짝수가 아닙니다")


print("[짝수]")
printEven(numbers)

print("[중앙값]")
printmedium(numbers)
