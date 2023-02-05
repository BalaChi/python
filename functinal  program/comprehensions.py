# easy  way to create list,set,dict
# istead of using for to append or anything

# Syntax: [param for param in iterable]
# param can be varialbe or anythin


# ******
"""list = []
for i in "hello":
    list.append(i)"""
# *******


list1 = [char for   char in 'helloi']

list2 = [num*2 for num in range(0,100)]

list3 = [num**2 for num in range(0,100)
if num % 2 == 0]
print(list3)

# num can be variable or a expersion

# ****** exercise *********
some_list = ['a','b','c','b','d','m','n','n']

# chech and find duplicates

duplicates = list(set([dup for dup in some_list if some_list.count(dup) > 1]))
print(duplicates)