# easiest way to read,write,append a file witout writing the f.close()
with open("monish.txt","r") as f:
    for line in f:
        print(line)
    # (or)
    c=f.read()
    print(c)
    
    
with open("monish3.txt","w") as f:
    f.write("hellooooooooooooooooooooooo")    
    
with open("monish3.txt","a") as f:
    f.write("sirrrrrrrrrrrrrrrrrrrrrrrrr")    