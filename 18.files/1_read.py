file=open("monish.txt","r") # here it refers to file and saying what to do r for reading

c=file.read() # it will says to read a file
print(c)
file.close() # without file.close() readimg is not completed



# ************************read line by line ************************

f=open("monish.txt",'r')

for line in f:
    print(line) #it read line by line
   #prinr(line.strip())---->it will remove the extra line

f.close()    