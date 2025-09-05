

from math import *
def add(x,y):
    return x+y
def sub(x,y):
            return x-y
while True:
    try:
        print("********* A simple calculator*************")
        print("**********************witbaynes program************")
        print("choose your operations")
        print( "1. Addition\n","2. subtraction\n","3. multiplication\n","4. division")
        choice=input("enter the operation you want to perform:")
        if choice not in ("1","2","3","4"):
              print("wrong input")
              continue
        num1=float(input("enter the first number"))
        num2=float(input("enter the second number"))
        
        if choice== "1":
            print(f"your answer is{add(num1,num2)}")
        elif choice=="2":
              print(f"your answer is :{sub(num1,num2)}")
        elif choice=="3":
              print(f"your answeer is:{ mul(num1,num2)}")
        elif choice =="4":
              if num2==0:
                    print("infinite number")
        else:
                    print(f"your answer is:{div(num1,num2)}")
        break
    except ValueError:#it will take anything thta is not value as an error
            print("invalid input,pls try again")
        




