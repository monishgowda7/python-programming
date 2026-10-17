def decorator(fun):
    def wrapper():
        print("boring")
        fun()
        print("boar athaitheee")
    return wrapper        
    
@decorator 
def greeting():
    print("namaskara!!!!")   
    
'''the actually function is looks like
 
        print("boring")
        print("namaskara!!!!")
        print("boar athaitheee")
'''   
    
greeting()    




# def div(a,b):
#     return a/b

# there is function div that we can make a change in div function without touching that function by using decorators

def function(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

@function
def div(a,b):
    return a/b


print(div(2,4))
  

