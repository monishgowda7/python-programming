class animal:  # parent class
    location="india"
    
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        
    def speak(self):
        return "its speaking like"
    
class dog(animal): # inherited class
    def spoke(self):
        print("bhow bhow")
        super().speak() # this is used to print the function statement from parent class


d=animal("dog","huskey")   
print(d.name)
print(d.breed)
d.speak()

a=dog("dogesh","huskey")
print(a.name)
print(a.breed)
a.speak()  # this will also print the statement from parent class
a.spoke()
print(a.location)
