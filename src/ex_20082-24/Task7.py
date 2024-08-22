# write a program to find the leap year
year = int(input("Please enter the Year"))
print(year)
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print("It is a Leap Year")
else:
    print("Not a leap year")