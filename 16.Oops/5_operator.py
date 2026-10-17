class point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        
        
    def sum(self,anself):
        return point((self.x+ anself.x),(self.y+anself.y))
    
    # *********(or)********
        
    def __add__(self,anself):
        return point((self.x+ anself.x),(self.y+anself.y))
        
    def finalpoint(self):
        print(f"the X is {self.x},the Y is {self.y}")    
     
            
        
p1=point(4,6)           
p2=point(1,9)    

p=p1.sum(p2)  # returns the point which has a sum p1+p2
p.finalpoint()

# (or)

p=p1+p2
p.finalpoint()
     
     
     
     
class point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        
        
    def sum(self,anself):
        return (self.x+ anself.x),(self.y+anself.y)
    
    # *********(or)********
        
    def __add__(self,anself):
        return (self.x+ anself.x),(self.y+anself.y)
        
    
p=point(1,2)
q=point(2,3) 
       
print(p.sum(q))     

print(p+q)