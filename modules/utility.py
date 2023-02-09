#generate random number
from random import randint
import sys
sys.argv
answer = randint(int(sys.argv[1]), int(sys.argv[2]))


#check

while True:
    try:
        #get input
        print(answer)        
        guess = input("guess a number")
        if int(guess) > 0 and int(guess) < 11:
            if int(guess) == answer:
                print("your ate correct")    
                break
        else:
            print("enter 1 to 10")
    except ValueError:
            print("plese neter number")
            pass




#         def add(num1,num2):
#     return num1+num2

# def div(num1,num2):
#     return num1/num2


# import sys
# x = sys.argv[1]
# print(f"x is {x}")


