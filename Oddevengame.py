
import random
import sys

def OddEven(even, odd, falsess):
    print("\n Can you guess whether my number is odd or even? If you can guess it, I will help you through this forest \n")
    num = random.randint(0, 10)

    #print(num)

    answer = input("your number is (even/odd)")

    
    if(num % 2 == 0 and answer =="even"):
        #print ("Yes, my number is " + str(num) + ", even number! You are the person sent by the god!")
        result = even
    elif(num % 2 == 1 and answer =="odd"):
        #print("Yes, my number is " + str(num) + ", odd number! You are the person sent by the god!") 
        result = odd
    else :
        #print("No.. you should go back your place. My number was " + str(num) )    
        result = falsess

    return result