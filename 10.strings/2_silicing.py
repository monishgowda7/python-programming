name = "monish123456789"
# name='m o n i s h 1 2 3 4  5  6  7  8  9'
#       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

print(name[0:10])  # print from 0 to 10-1
print(name[0:15])
print(name[0:-6])  # [-6+15]=9, and 9-1=8 means from 0 to 8


# print(name[0:15:n]) #means skipping n-1 character consegatively
print(name[0:14:1])  # means skipping 1-1=0 ,nothing will happens her
print(name[0:15:2])  # means skipping 2-1=0,skipps 1 character consegatively
#  output=mns13579 ,it skips concegatively one number

print(name[0:15:3])  # means skipping 3-1=2,skipps 2 character consegatively
#  output=mi147 ,it skips concegatively one number


print(name[:10])  # it will take 1st number as 0
print(name[0:])  # it will take 2nd number as length of a string
print(name[:]) 