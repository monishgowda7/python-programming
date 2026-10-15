name = "monish gowda"  # strings are immutable

# name[0]='r'------->u cant do this

print(len(name))  # to know the length of the string

print(name.upper())  # upper the case
print(name.lower())  # lower the case
print(name.capitalize())  # make caps of 1st letter of a word
print(name.title())  # make caps of 1st letter of every word

hii = " \n monish gowda "

print(hii.strip())  # it will remove new line and space from left and right
print(hii.lstrip())  # it will remove new line and space towards left
print(hii.rstrip())  # it remove in right


a ="your name is this and this"
print(a.find("and"))  # it will find the string number of 1st console of that letter
print(a.replace("this", "that"))  # it will replace the letter


g='apples,orange,graps'   
print(g.split(','))  #converts string to lists
print(",".join(['apples', 'orange', 'graps'])) #coverts list to string


m = "thenameismonish7"
# it will give output through boolean
print(m.isdigit())  # contains only digits
print(m.isalnum())  # contains alphabeat and numbers/digits
print(m.isspace())
print(m.isalpha())

print(m.count("o")) # it tells how many times a element as apperas
 
 
