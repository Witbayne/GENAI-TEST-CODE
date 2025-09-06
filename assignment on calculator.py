from math import *
def add(x,y):
      return x+y
def sub(x,y):
      return x-y
def mul(x,y):
      return x*y
def div(x,y):
      return x/y
def pow(x,y):
      return x**y

while True:
    try:#it is a block of code that run the code if there is an error
        print("********* A simple calculator*************")
        print("**********************witbaynes program************")
        print("choose your operations")
        print( "1. Addition\n","2. subtraction\n","3. multiplication\n","4. Exponenetial\n","5. division\n","6. squareRoot\n","7. press 7 to end\n")
        choice=input("enter the operation you want to perform:")
        if choice not in ("1","2","3","4","5","6","7"):
            print("wrong input")
            continue #it will take you to the start of the loop if the input is wrong
        elif choice=="7":
             print(f"end of program")
             break
        if choice=="6":
            num3=float(input("enter the num to finf the root"))
            print(f"your answer is:{sqrt(num3)}") 
            break#it will break the  loop to stop the code from continuing after a successful trial
        num1=float(input("enter the first number:"))
        num2=float(input("enter the second number/power number:"))
        if choice== "1":
            print(f"your answer is{add(num1,num2)}")
        elif choice=="2":
            print(f"your answer is :{sub(num1,num2)}")
        elif choice=="3":
            print(f"your answeer is:{ mul(num1,num2)}")
        elif choice=="4":
            print(f"your answer is:{pow(num1,num2)}")
        elif choice =="5":
            if num2==0:
                print("infinite number")
            else:
                print(f"your answer is:{div(num1,num2)}")
        break
    except ValueError:#it will take anything thta is not value as an error
        print("invalid input,pls try again")