# lists are ordered,mutable(changable) collections of items

a=[9,18,27,36,45]
b=[99,'hello',True,'true','m']
#  0    1      2     3     4

a[1]=19 # we can change the lists a[index]=what value u want to replace
print(a)
print(a[0]) # same as string in lists starts with 0 1 2 3..
print(a[3])
print(b[4])
print(b[3])

# we can also slice the list as string

print(a[0:3])
print(a[0:-2])
print(b[1:4])
print(b[0:5])