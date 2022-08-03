print("버스 요금 계산기")

inp_age = int(input("나이를 입력해 주세요: "))
inp_payment = str(input("카드 또는 현금으로 지불유형을 입력하여 주세요: "))
print("나이: ",inp_age, "세")
print("지불유형: ", inp_payment)

def bus_fare(age, payment):
    if age < 8:
        print("버스요금: 무료")
    elif age <14:
        if payment=="카드":
            print("버스요금: 450원")
        elif payment=="현금":
            print("버스요금: 450원")
        else:
            print("잘못된 입력입니다.")
    elif age <20:
        if payment=="카드":
            print("버스요금: 720원")
        elif payment=="현금":
            print("버스요금: 1000원")
        else:
            print("잘못된 입력입니다.")
    elif age <75:
        if payment=="카드":
            print("버스요금: 1200원")
        elif payment=="현금":
            print("버스요금: 1300원")
        else:
            print("잘못된 입력입니다.")
    else :
        print("버스요금 : 무료")
         

bus_fare(inp_age, inp_payment)
