# args will be tuple that will take the all values passed to function in the form of tuple
def multi(*args):
    total=0
    for item in args:
        total+=item
    return total
    
print(multi(5,6,9)) 
 
