import re
text="A black cat jumps on the lazy dog"
# https://regexr.com/

m=re.search("black",text)  # it will search the index of given word
print(m)
print("starting index:",m.start())
print("ending index:",m.end())


n=re.findall("c",text,re.IGNORECASE)  # it will find word given 
print(n)


o=re.sub("cat","rat",text) # it will repalace the word
print(o)


