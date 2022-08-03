monthly_payment = int(input("현재 월급을 입력해주세요. : "))

def yearly_payment(money):
    before_tax = money * 12
    if before_tax < 1200:
        since_tax = int(before_tax - (before_tax * 0.06))
        print("세전 연봉 : ", before_tax, "만 원")
        print("세후 연봉 : ", since_tax, "만 원")
    elif before_tax < 4600:
        since_tax = int(before_tax - (before_tax * 0.15))
        print("세전 연봉 : ", before_tax, "만 원")
        print("세후 연봉 : ", since_tax, "만 원")
    elif before_tax < 8800:
        since_tax = int(before_tax - (before_tax * 0.24))
        print("세전 연봉 : ", before_tax, "만 원")
        print("세후 연봉 : ", since_tax, "만 원")
    elif before_tax < 15000:
        since_tax = int(before_tax - (before_tax * 0.35))
        print("세전 연봉 : ", before_tax, "만 원")
        print("세후 연봉 : ", since_tax, "만 원")
    elif before_tax < 30000:
        since_tax = int(before_tax - (before_tax * 0.38))
        print("세전 연봉 : ", before_tax, "만 원")
        print("세후 연봉 : ", since_tax, "만 원")
    elif before_tax < 50000:
        since_tax = int(before_tax - (before_tax * 0.4))
        print("세전 연봉 : ", before_tax, "만 원")
        print("세후 연봉 : ", since_tax, "만 원")
    else:
        since_tax = int(before_tax - (before_tax * 0.42))
        print("세전 연봉 : ", before_tax, "만 원")
        print("세후 연봉 : ", since_tax, "만 원")

yearly_payment(monthly_payment)
