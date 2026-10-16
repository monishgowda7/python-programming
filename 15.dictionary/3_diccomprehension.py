squares={x:x**2 for x in range(1,11) }
print(squares)

dict1={"name":"monish","age":19}
dict2={"college":"bms"}
merge={**dict1,**dict2} # use to merge the two dict,if key are same both the dict then second dict value will overwrite the 1st dic value 
merge=dict1 | dict2
print(merge)


'''lists=ordered,mutable
   tuples=orderd,immutable
   sets=unorderd,unique
   dictionary=key value pairs
'''