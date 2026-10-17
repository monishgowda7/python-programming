class employee:
    company="hp"
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
     
    # this is instance method
    def hii(self):
        return f"my name is {self.name},my salary is {self.salary}"  
    
    # this is static method,used in the function to solve the pproblem without using self
    @staticmethod
    def add(a,b):
        return a+b 
    
    # this is class method it will used to change class or instance attribute 1st priority instance 2nd priority class
    @classmethod
    def info(cls,newcom):
        newname=newcom
        cls.company=newname
        
    # we can also solve by this method
    def info_i(self,newcom):
        newname=newcom
        employee.company=newname
        
   
    
e1=employee("preetam",1000000000000)   
# print(e1.salary) 
# print(e1.hii())
print(e1.add(4,6))
print(e1.company)
e1.info("asus")
print(e1.company)
        
    
    