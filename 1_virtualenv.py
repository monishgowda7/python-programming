# to install modules------->pip install 

# global envirnoment and virtual envirnoment(it is a fresh start for a code)
# to install virtual envinoment--->pip install virtualenv

# to create a virtual envirnoment to file--->python -m virtualenv env1
# above virtualenv is the file to which we want to create virtual envinoment and env1 is virtual envinoment name

# to activate the virtual envinoment--->env1\Scripts\Activate.ps1


# after activating virtual env is fresh it we intall modules in it
# ex:pip install pandas
# we can install specific version of modules ex:pip install pandas==1.20.0

# to see packages installed in the virtual envirnoment--->pip list

# to upgrade the package--->pip install --upgrade filename

# to uninstall package--->pip uninstall filename


# to make all the installed packages in txt form--->pip freeze > requirement.txt
# to install that packages by someone that you have installed either by installing one by one manually or by using--->pip install -r requirement.txt

# to deactivate the virtual envirnoment--->deactivate