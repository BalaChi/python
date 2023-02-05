#   an anonymoues function can be used only once
my_list = [1,2,3]
#insted of usng functions we can  use lambda
print(list(map(lambda item: item % 2 != 0,my_list)))
print(my_list)

#exercise for lambda

#squaring list using  lambda

list1 = [2,3,4]

print(list(map(lambda item: item**2,list1)))

# list sorting

a = [(0,2),(4,3),(10,-1),(9,9)]

# sorting based on second item
# x -- arameters it can be anyting basically it applies on a

a.sort(key = lambda x: x[1])
print(a)