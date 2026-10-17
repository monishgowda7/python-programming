import shutil

# # removes the directory
shutil.rmtree("new2_directory")

# copies text from monish2.txt and paste in monish.txt and removes the whatever previous text in monish.txt
shutil.copy("monish2.txt","monish.txt")

# to move a file or directory
shutil.move("new_directory","directory")
shutil.move("monish.txt","directory")