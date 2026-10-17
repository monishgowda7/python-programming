class employee:
    company="lenovo" # this is a class attribute
    
    def __init__(self,name,salary,status,increment,company):
        self.name=name
        self.salary=salary
        self.status=status
        self.increment=increment
        self.company=company
    
    def info(self):
        return f"ur name is {self.name},ur salary is {self.salary},ur status is {self.status},ur increment this year is {self.increment}"
    
e1=employee("preetam",30000000,"permanent employee",5000000,"asus")
print(e1.company)  # this is instance attribute, in this case it will print
print(employee.company) # now class attribute will print


# this is "object intropection" will print the possible methods 
print(dir(e1))