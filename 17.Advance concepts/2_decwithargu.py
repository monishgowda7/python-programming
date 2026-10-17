def loop(n):
    def decorator(fun):
        def wrapper(y):
            for i in range(n):
                    fun(y)      
        return wrapper
    return decorator      
                    
                    
@loop(5)
def greeting(y):
    print("namaskara!!!!!")    
    
greeting("hii")    


''' 
def decorator(fun):
        def wrapper(y):
            for i in range(n):
               greeting(y)


'''                