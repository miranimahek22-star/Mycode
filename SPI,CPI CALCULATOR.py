def calculate_spi(n):
    totalcredits = 0
    totalpoints = 0
    for i in range(n):
        name=input(f"Enter subject name {i+1} : ")
        credit = int(input(f"Enter total credits of {name} : "))
        while True:
            grade = input(f"Enter grade obtained in  {name}(O,A+,A,B+,B,C,D) : ").strip().upper()
            point = 0
            if grade == 'O':
               point +=credit*10
            elif grade == 'A+':
               point +=credit*9
            elif grade == 'A':
               point +=credit*8
            elif grade == 'B+':
               point +=credit*7
            elif grade == 'B':
               point +=credit*6
            elif grade == 'C':
               point +=credit*5
            elif grade == 'D':
               point +=credit*0
            else:
               print("Invalid grade entered. Please enter a valid grade.")
               continue
            totalpoints += point
            totalcredits += credit
            break
    spi=totalpoints/totalcredits
    print(f"SPI: {spi:.2f}")
    return spi,totalpoints,totalcredits
print("----------FIRST SEMESTER----------")
n1=int(input("Enter number of subjects in first semester: "))
spi1,totalpoints1,totalcredits1=calculate_spi(n1)
print("----------SECOND SEMESTER----------")
n2=int(input("Enter number of subjects in second semester: "))
spi2,totalpoints2,totalcredits2=calculate_spi(n2)
print("----------OVERALL RESULT(CPI)----------")
cpi=(totalpoints1+totalpoints2)/(totalcredits1+totalcredits2)
print(f"CPI: {cpi:.2f}")
if spi1<5 or spi2<5:
    print("FAIL")
    if spi1<5 and spi2<5:
        print("You should score spi greater than or equal to 5 in both semesters to pass the semester.")
    elif spi1<5:
        print("You should score spi greater than or equal to 5 in first semester to pass the semester.")       
    else:
        print("You should score spi greater than or equal to 5 in second semester to pass the semester.")
elif cpi>=9:
    print("Congratulations! You are in the top 10% of your class.")
elif cpi>=8:
    print("Congratulations! You are in the top 20% of your class.")
    print(f"You need {9-cpi} more points to reach the top 10% of your class.")
elif cpi>=7:
    print("Congratulations! You are in the top 30% of your class.")
    print(f"You need {9-cpi} more points to reach the top 10% of your class.")
elif cpi>=6:
    print("Congratulations! You are in the top 40% of your class.")
    print(f"You need {9-cpi} more points to reach the top 10% of your class.")
elif cpi>=5:
    print("Congratulations! You are in the top 50% of your class.")
    print(f"You need {9-cpi} more points to reach the top 10% of your class.")
else:
    print("FAIL")
    print("You should score cpi greater than or equal to 5 to pass the semester.")