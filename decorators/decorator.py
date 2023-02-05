# def hello():
#     print("vlknerbler")

# greet = hello
# del hello
# # del hello just delets the word nor func becoz it is pointed bt another vaiable
# # here greet means not kalling just gives the location of func
# print(greet())



# # ********

# def hllo1(func):  #higher order function (func accepts anither func or returns)

#     # coz of this greet is called
#     func()

# def greet1():
#     print("helo")

# a = hello(greet)


# *******

# DECORATOR STARTS


def my_decorator(func):
    def wrap_func(x):
        print("*********88")
        func(x)
        print("***********8")

    return wrap_func

@my_decorator 
def hello1(greeting):
    print(greeting)
hello1("hiii")


""" hello2 = my_decorator(hello)
 print(hello2) --- insted of this wraping hello func in my decorator we use @decoroto simpkly"""


# synatx
# # def my_decoraator(func):
#     def wrap():
#         func(*args,**kwargs)
#     return wrap
# @my_decoraator
# def hello(greeting,emoji="))"):
#     print(greeting,emoji)
# hello1("vrni")







