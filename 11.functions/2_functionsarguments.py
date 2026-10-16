def sum(a, b, plus):
    return a + b - plus


i = sum(10, 4)  # here plus is optional
print(i)

i = sum(10, 4, 4)  # if u wrote the 3rd number so plus is considered
print(i)


def sum(a, b):
    return a + b


i = sum(b=4, a=10)  # taking value of a and b is not compulsarily in order u want to  mention which is a values and b values if u are not taking in order
print(i)
