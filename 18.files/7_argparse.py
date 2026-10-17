import argparse

a=argparse.ArgumentParser(description="simple calculator")

a.add_argument("num1",type=float,help="first number")
a.add_argument("num2",type=float,help="second number")
a.add_argument("operation",choices=["add","sub","mul","div"],help="operation to perform")

b=a.parse_args()

if(b.operation == "add"):
    print(f"the addition of two number is {b.num1+b.num2}")
elif(b.operation == "sub"):
    print(f"the subtration of two number is {b.num1-b.num2}")
elif(b.operation == "mul"):
    print(f"the multiplication of two number is {b.num1*b.num2}")
elif(b.operation == "div"):
    print(f"the division of two number is {b.num1/b.num2}")
else:
    print("enter a valid operation") 