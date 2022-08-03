print("학점 변환기")

inp_name = str(input("이름을 입력해 주세요: "))
inp_score = int(input("점수를 입력해 주세요: "))

def grade(name, score):
    print("학생이름: ", name)
    print("점수: ", score, "점")
    if(score >= 95):
        print("학점: A+")
    elif(score >= 90):
        print("학점: A")
    elif(score >= 85):
        print("학점: B+")
    elif(score >= 80):
        print("학점: B")
    elif(score >= 75):
        print("학점: C+")
    elif(score >= 70):
        print("학점: C")
    elif(score >= 65):
        print("학점: D+")
    elif(score >= 60):
        print("학점: D")
    else:
        print("학점: F")


grade(inp_name, inp_score)
