from functools import reduce

a=[1,2,3,4,5,6,7,8,9]  # reduce work is acutally look like this
#   [3,3,4,5,6,7,8,9]
#   [6,4,5,6,7,8,9]
#   [10,5,6,7,8,9]
#   [15,6,7,8,9]
#   [21,7,8,9]
#   [28,8,9]
#   [34,9]
#   [45]
def sum(x,y):
    return x+y

z=reduce(sum,a)
print(z)


x=[3,4,6,4,67,3,7,3,7,43,67]

def div(x,y):
    return x/y

s=reduce(div,x)
print(s)