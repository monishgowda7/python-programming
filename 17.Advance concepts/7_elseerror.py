try:
    a=int(input("enter a 1st number:"))
    b=int(input("enter a 2nd number:"))
    c=a/b
    print(c)
  
except Exception as e:
    print("there is a error called," ,e)   
    
    
# here "else" will only print if there is no error in upper part    
else:
    print("hey you did no errors")     
      