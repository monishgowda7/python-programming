num=[12,43,5,6,3,6,4,6,653]

def grea9(x):
    if x>9:
        return True
    else:
        return False
    
# here filter has seperated the elements which is true
c=list(filter(grea9,num))    
print(c)


def evennum(x):
    if x%2==0:
        return True
    else:
        return False
    
z=[5,54,98,8,765,6,98,765,5,67,98,765,98,76,8,9,876,7,9,876,789,87,6]  
v=list(filter(evennum,z))      
print(v)



