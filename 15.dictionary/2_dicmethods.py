a={'me':0,'others':100}
print(type(a))

print(a.keys())
print(a.values())

a.pop("others") # removes the others key
print(a)

print(a.items()) # seperate each pair of elements

print(a.clear()) # clears the dictionary

