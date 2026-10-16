def bword(name):
    global z #if we want to print local z then we want declare like global z
    z=45  #then this will become a global variable
    return f"bolimaga yaru adu,{name}"

z=10
print(bword("preetam"))
print(z)

# excessive use of global is discouarged as it make debugging harder