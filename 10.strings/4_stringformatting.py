#string formtting

template="my dear{},you won the lottery price of {}rs"
a='avnu'
a1=10000
b='evnu'
b1=1
c='aatha'
c1=100000000000000000

print(f"my dear {a},you won the lottery price of {a1}rs")
print(f"my dear {b},you won the lottery price of {b1}rs")
print(f"my dear {c},you won the lottery price of {c1}rs")

text='python'
print(f"{text:^10}") #centre align 
print(f"{text:>10}") #right align
print(f"{text:<10}") #left align
#outputs:/
#  python
#     python
# python
print(text.encode()) # converts string into bytes object
