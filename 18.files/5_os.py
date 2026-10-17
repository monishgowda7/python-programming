import os

# this will show the files and sub directory in DIRECTORY
a=os.listdir("directory")
print(a)

# to get current working directory
b=os.getcwd()
print(b)

# to check wheather directory is exist or not in bollen form
c=os.path.exists("directory")
print(c)


# to remove the files but not directory
os.remove("hmm.txt")

# to remove empty directory
os.rmdir("directory")

#  to make a new directory
os.mkdir("new_directory")  
os.makedirs("path/to/new2_directory")  # creates nested directory path inside it "to" inside "to" is new2_directory


# change the current directory
os.chdir("new_directory")
print(os.listdir())

# rename the file
os.rename("hello.txt","helo.txt")


