number = int(input("몇단? : "))
print(number, "단")

for i in (1,3,5,7,9):
#for i in (1,3,5,7,9,11,13,15,17,19):
    multi = number * i
    if multi<=50:
        print(number, "*", i, "=", multi)
