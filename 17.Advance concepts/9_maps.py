# map will apply the given function to given every element of list here
num=[1,2,3,4,5,6,7]

def mul(x):
    return x*x

def div(x):
    return x/2

b=list(map(div,num))
print(b)

c=list(map(mul,num))
print(c)

# mapping is used to map the two things
a=list(map(lambda x:x**2,num))
print(a)

