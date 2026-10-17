try:
    
    a=int(input("enter a 1st number:"))
    b=int(input("enter a 2nd number:"))
    print(f"the division is {a/b}")
    
except ValueError:
    print("sisya,number type maduu!!",) 
    
except ZeroDivisionError:
    print("sisya,zero inda divisible agalla!!")    
    
# except: this will also pass error 
except Exception as e:
    print("error ede kano gubee,",e)   # e will print what type of error 
    
    
    
    
    
    

x=int(input("enter a 1st number:"))
y=int(input("enter a 2nd number:"))  
    
# raise error is used because to stop other developer to misuse ur code.and it will crash the code

if -1000000000000000000000<=y<=1000000000000000000000000:
    raise ZeroDivisionError("error occured")

print(f"the division of two number is {x/y}")
    
    