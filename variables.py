def variables_practice():
    ageMon=str(219)
    yearDays=str(365)
    firstPet="Miso"
    piFive=str(3.1415)
    
    print(ageMon,yearDays,firstPet,piFive)

def expressions_practice():
    fruits=str("apples")
    totalStudents=int(16+12)
    noOfApples=int(5**3)
    studentsShare=int(noOfApples//totalStudents)
    leftover=int(noOfApples%totalStudents)
    totalTeachers=int(((30-12)+24)*2)
    veganTeachers=int(((totalTeachers/2)+12/1.8)//2)

    print(totalStudents,noOfApples,fruits,studentsShare,leftover,totalTeachers,veganTeachers)

def prompt_print():
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    print("sum: "+str(num1+num2))
    print("difference: "+str(num1-num2))
    print("product: "+str(float(num1*num2)))
    print("quotient: "+str(float(num1/num2)))

variables_practice()
expressions_practice()
prompt_print()