def marks(**kurgs):
    # kurgs is a dictionary that will take all key value pairs passes to function in the form of dictionary 
    for item in kurgs.keys():
      print(f"the marks of {item} is {kurgs[item]}")
      # print(kurgs)
    
marks(he=45,she=67,hiiii=76)
