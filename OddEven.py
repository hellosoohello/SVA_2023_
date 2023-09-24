import random
import sys
import os
import time
import imgs
import Oddevengame


player = {
    "name" : "p1",
    "score": 0,
    "location": "start"
}

scene = {
    "scene1" : "forest",
    "scene2" : "painful",
    "scene3" : "people"
}


def intro():
    os.system('clear')
    print("\n There's a thumping sound!!!!! \n")
    time.sleep(5.2)
    imgs.StartGame("Crushing")
    time.sleep(3.2)
    print("One day, you took a plane to go somewhere, but the flight had an accident and crashed into an unknown forest.")
    print("Suddenly, after this happened, you realized that you could understand other animals’ conversations. \n")
    time.sleep(3.2)   
    imgs.StartGame("gorilla")
    
    print("There is a group gorillas coming towards you.")
    playerInput = input("Do you want to talk with them or do you try to avoid them? (talk / avoid)")

    if(playerInput == "talk"):
        os.system('clear')
        print("Kwame: Are you a human?")
        print("Esi: (anxiety on her face)")
        print("Kwame: Esi, we don't have any choices.")
        print("Esi: Then let's play a simple game to check if he was sent by the god.") 
        print("Kwame: Hmm.")
        print("Esi: Just something simple.")
        print("Kwame: Okay, don't be afraid.\n")
        OddEven()


    else:
        print("You missed a chance to survive in the forest")
        #intro()


    # the player canoose yes or no
    if (playerInput == "yes"):
        print ("You walk down the path, it leads into a forest clearing...")
        input("press enter >")
        #forestClearing()
  


def OddEven():
    print("\n Can you guess whether my number is odd or even? If you can guess it, I will help you through this forest \n")
    num = random.randint(0, 10)

    #print(num)

    answer = input("your number is (even/odd)")

    
    if(num % 2 == 0 and answer =="even"):
        print ("Yes, my number is " + str(num) + ", even number! You are the person sent by the god!")
        #result = even
    elif(num % 2 == 1 and answer =="odd"):
        print("Yes, my number is " + str(num) + ", odd number! You are the person sent by the god!") 
        #result = odd
    else :
        print("No.. you should go back your place. My number was " + str(num) )    
        #result = falsess

    #return result

def main():
    imgs.StartGame("title")

    intro()


main()
