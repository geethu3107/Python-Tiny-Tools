#Number Guessing Game
import random
secret_number=random.randint(1,10)
count=1
while count<=3:
    num=int(input("Enter guess:"))
    if num<1 or num>10:
        print("Guess out of range")
        count=count+1
        continue
    elif num==secret_number:
        print("Congratulations , You Won")
        break
    elif num>secret_number:
        print("Oops! You crossed it!")
    elif num<secret_number:
        print("Oops! You are lagging behind ")
    count=count+1
else:
    print("Better luck next time!")
    
#Multiplication Table Generator
n=int(input("Enter number:"))
for i in range(1,11):
    result=n*i
    print(f"{n} x {i} = {result}")

#BMI Calculator
weight=float(input("Enter your weight in Kg:"))
height=float(input("Enter your height in meters:"))
def calculate_bmi(weight,height):
    bmi= weight/(height**2)
    return bmi
result=calculate_bmi(weight,height)
print(f"Your BMI is: {result}")


