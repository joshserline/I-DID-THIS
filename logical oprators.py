# logical operators (and,or,not) = used to check of two or more conditiona; statement

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("the tempreture is good today!")
    print("go outside!")
elif not(temp <0 or temp >30):
    print("the tempreture is bad today!")
    print("stay inside!")