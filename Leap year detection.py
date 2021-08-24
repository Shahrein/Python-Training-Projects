

year = int(input("Enter a year: "))
leap_cond_1 = (year % 4)

if year < 1581:
    print("Not Within the Gregorian Calender Period")
elif leap_cond_1 == 0:
    print("leap year")
else:
    print("Common Year")