class employee:
    
    def __init__(self,name,salary,status,increment):    # this is constructors
        self.name=name
        self.salary=salary
        self.status=status
        self.increment=increment
    
    def info(self):
        return f"ur name is {self.name},ur salary is {self.salary},ur status is {self.status},ur increment this year is {self.increment}"
    
e1=employee("preetam",30000000,"permanent employee",5000000)
print(e1.salary)
print(e1.name)
print(e1.increment)
print(e1.info())