a=int(input("enter a 1st number:"))
b=int(input("enter a 2nd number:"))

try:
    
    print(f"the division of two number {a/b}")
    
except Exception as e:
    print("there ia error called",e)
    
# finally is always executed wheather try is executed completely or not

finally:
    print("hello bhai!!!")    
      
    
