# core concept genrators
# working of for loop
def special_for(iterable):
    iterator = iter(iterable)
    print(type(f"xx is {special_for}"))
    while True:
        try:
            print(iterator)
            print(type(next(iterator))) #give the item
        except StopIteration:
            break
special_for([1,2,3])
