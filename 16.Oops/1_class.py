# class is like reference,for ex :u have a class design this is a class

# object when u make a car like BMW,MERCEDES,TESLA by using class a that reference,now they are become a object


class employee:
    company = "ur company name is:HP"

    def salary(self):
        return "ur salary is:30000"


e1 = employee()
print(e1.salary())
print(e1.company)

e2 = employee()
print(e2.salary())
print(e2.company)
