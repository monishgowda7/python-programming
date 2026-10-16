# there are two types of modules 
# 1.built in modules
# 2.external modules 
# built in modules---->https://docs.python.org/3/py-modindex.html


import math  #we can import external module
import requests #we can install external module through pip
import mymodule #we can import our own module

print(math.sqrt(100))
print(mymodule.greet())
r=requests.get("https://www.google.com") #we will learn this in future
print(r.text)

