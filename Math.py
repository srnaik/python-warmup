import math

print(10+3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)
print(round(2.9))
print(round(2.6))
print(abs(-2.9))

print(math.ceil(2.9))


x = input("x: ")
print(type(x))
y = int(x)+1
print(f"x: {x}, y: {y}")

temprature = 35

if temprature > 30 :
    print("It's warm")
    print("Drink Water!!")
print("It's ok")

age = 22

message = "Eligible" if age >= 12 else "Not Eligible"
print(message)

# Logical Operators ->  'and' 'or' 'not'

high_income = True
good_credit = True


if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")