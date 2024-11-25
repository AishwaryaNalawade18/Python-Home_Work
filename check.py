age=int(input("enter the age: "))
if age<=12:
    print("kid")
elif 12<age<18:
    print("teen")
elif 18<=age<60:
    print("adult")
else:
    print("senior")