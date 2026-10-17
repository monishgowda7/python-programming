#  You can use obj.name instead of obj.get_name() and obj.set_name(), making the code cleaner and more readable by using "getter(here property) decorator"

class employee:
    
    def __init__(self,name):
        self.name=name
     
    @property           # getter
    def fullname(self):
        m=self.name.split(" ")
        print(m)
        return m[0]
    
    @fullname.setter     # setter
    def fullname(self,changename):
        m=self.name.split(" ")
        newname=f"{changename} {m[1]}"
        self.name=newname




e1=employee("preetam kumar")
e1.fullname
e1.fullname="prem"
print(e1.name)

