sets = { 45, 54, 76, 69,}

sets.add(1)
print(sets)
# add the 1 to in any order of a set
sets.remove(54)
print(sets)
# removes 54 from a sets
# print(sets.remove(54637))  # it will show an error if the element is not present in the sets
sets.discard(785678976)
print(sets)
# it won't show an error if element is not present in the set , if present it will remove
sets.pop()
print(sets)
# removes an random element


