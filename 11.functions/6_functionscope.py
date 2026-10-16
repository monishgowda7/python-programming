def multi(a,b):
    x=99 #this is the local varible which destroys it self after return of def code
    return a*b

x=18 #this is the global variable intrepreter will print global value
print(multi(3,3))
print(x)








