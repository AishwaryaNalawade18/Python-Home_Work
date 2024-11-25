# Write a program to check if a given number is positive , negative or zero.
# num=5
# if num < 0:
#     print("Negative")
    
# elif num > 0:
#     print("positive")
# else:
#     print("Zero")


# write a program to check if a given number is odd or even
# n = int(input("enter a number:"))
# if (n % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

#Grade Checker
# per=int(input("Enter your percentage between(1-100): "))
# if 90 <= per <= 100:
#     print("A")
# elif 70 <= per < 90:
#     print("B")
# elif 50 <= per <=70:
#     print("C")
# else:
#     print("D")


# Check Divisibility
# num=int(input("enter a number: "))
# if num % 3==0 and num % 5==0:
#     print("Divisible by both 3 and 5")
# elif num % 3==0 :
#     print("Divisible by 3")
# elif num % 5==0 :
#     print("Divisible by 5 ")
# else :
#     print("Not Divisible By 3 or 5")


# find the minimum number between two numbers
# num1=int(input("enter 1st number: "))
# num2=int(input("enter 2nd number: "))
# if num1 > num2:
#     print("Minimum number is ",num2)
# else:
#     print("Minimum number is ",num1)


# find the maximum number between three numbers
# a=int(input("enter 1st number: "))
# b=int(input("enter 2nd number: "))
# c=int(input("enter 3rd number: "))
# if a >= b and a >= c:
#     print("Largest no. is ", a)
# elif b >= a and b >= c:
#     print("Largest no. is ", b)
# else:
#     print("Largest no. is ", c)


# program to check Leap year
# year=int(input("Enter a year: "))
# if(year % 4==0 and year % 100 != 0) or year % 400==0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# Nested temperature check  
# temp=int(input("Enter temperature in celsius: "))
# if temp < 15:
#     print("Cold")
# elif 15 <= temp <=30:
#     print("Warm")
# else:
#     print("Hot")

# Vowel or Consonant
# char= input("Enter the character: ")
# if char in "aeiouAEIOU":
#     print("Vowel")
# elif char.isalpha():
#     print("Consonant")
# else:
#     print("It is not a alphabet")

# Driving eligibility
# age=int(input("Enter your age: "))
# if age >= 18:
#     lic=input("Do you have driving Licencse? (yes/no) : ")
#     if lic=="yes"or lic=="YES":
#         print("eligible to Drive")
#     else:
#         print("you need driving license for driving eligibility")
# else:
#     print("not eligible")

# Triangle validation
# a=int(input("Enter the three sides of tringle: "))
# b=int(input())
# c=int(input())
# if a+b > c and a+c > b and b+c >a:
#     print("Valid triangle")
# else :
#     print("It is not a valid triangle")

# Calculate tax based on salary
# tax=0
# salary=int(input("enter your salary : "))
# if salary <= 500000:
#     tax=salary*0.05
# elif 500000 < salary <= 1000000:
#     tax=salary*0.10
# elif salary >= 1000000:
#     tax= salary*0.20
# print("Tax is: ", tax)

# Categorize age
# age=int(input("Enter your age : "))
# if age <= 12:
#     print("Child")
# elif 12 < age <= 19:
#     print("Teen")
# elif 19 < age <= 59:
#     print("Adult")
# else:
#     print("Senior")

# Logical AND check

# num=int(input("Enter your num : "))
# if num >10 and num %2 ==0:
#     print("number is greater than 10 and divisible by 2")
# else :
#     print("number is not greater than 10 and not divisible by 2")

# logical OR check
# num=int(input("Enter your num : "))
# if num < 5 or num > 20:
#     print("Number is either less than 5 or greater than 20")
# else:
#     print ("condition does not satisfy")

# electricity bill
# bill=0
# unit=int(input("Enter the usage in unit : "))
# if unit <= 100:
#     bill = unit*5
# elif 100 < unit <=200:
#     bill = unit*10
# elif unit > 200:
#     bill =unit*15
# print("Electricity bill is : ",bill)


# season finder
# month=input("enter the month: ").lower()
# if month in ["dec","jan",'feb',"december","january", "february"]:
#     print("Winter")
# elif month in ["mar","apr","may","march","april"]:
#     print("Spring")
# elif month in ["jun","jul","aug","june","july","august"]:
#     print("Summer")
# elif month in ["sep","september","oct", "october","nov", "november"]:
#     print("Autumn")
# else:
#     print("invalid month")

# password validation
# password=input("enter your password : ")
# if len(password) >=8 and "@" in password:
#     print("Password is valid")
# else :
#     print("Password is invalid")

# categorize bmi
# bmi=float(input("enter your BMI : "))
# if bmi<18.5:
#     print("underweight")
# elif 18.5<= bmi<=24.9:
#     print("Normal")
# elif 25 <= bmi <=29.9:
#     print("Overweight")
# elif 30 <= bmi:
#     print("Obese")

# character type checker
char=input("enter the character: ")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("special character")