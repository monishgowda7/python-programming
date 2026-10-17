class airplane:
    def fly(self):
        print("aerplane will fly by using engines")
        
        
class bird:
    def fly(self):
        print("birds fly by their wings")
        
def flying(object):
    object.fly()
    
    
a=airplane()          
b=bird()

flying(a)
flying(b)