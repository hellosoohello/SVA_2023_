import random
import sys
import os
import time
import imgs
import Oddevengame


player = {
    "name" : "p1",
    "score": 0,
    "location": "start",
    "item": ["textbook", "laptop", "arduino"]
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
        print("\n You missed a chance to survive in the forest \n ")
        print(" Say good bye! \n No more game~~~\n")
        
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
        time.sleep(3.2)
        #result = even
        treatment()
    elif(num % 2 == 1 and answer =="odd"):
        print("Yes, my number is " + str(num) + ", odd number! You are the person sent by the god!") 
        time.sleep(3.2)
        treatment()        
        #result = odd
    else :
        print("No.. you should go back your place. My number was " + str(num) )  
        time.sleep(3.2)
        print("game over")  
        #result = falsess

    #return result

def treatment():
    os.system('clear')
    print("Following Kwame, there is a sick gorilla.")
    imgs.StartGame("sick")
    playerInput = input("Do you want to help or run away? (help/run)")

    if (playerInput == "help") :
        print("He gave you something. It looks precious, but it also appears to be of human origin")

        player["item"].append("preciousThings")
        print("\nYou : hmm,, are there any other humans around? \n")
        time.sleep(6.4)
        OnMyWay()

    else:
        print("\nYou lost your way.. ")
        print("Game Over")


def OnMyWay():
    os.system('clear')
    print("Still following Kwame, there is a path ahead..!")
    print("However, there's some noise around here. You can see some people over there.")
    print("Wait, they are armed and trying to attack the gorillas.")

    playerInput = input("\nDo you want to support them? Or just hide?(support/hide)")

    if(playerInput == "support") :
        os.system('clear')
        print("You: What happened? I heard that this area is an important place for gorillas...\n")
        print("Person 1: This area has various minerals, so we have to develop it. We got permission from the government too.")
        print("Person 2: We need money. We haven't received a salary in almost three months, and the boss said that when this area is developed, he can pay us.")
        print("\n")
        print("Kwame, Esi - (remain silent)")
        print("Why do people have to act like this? Why do they still need money even when they work hard...?\n")
        time.sleep(10.5)
        Ending()


    else:
        print("\nYou lost your way again.. ")
        print("Game Over")        

def Ending() :
    os.system('clear')
    print("In the Congo, labor is exploited to extract the core mineral coltan used in semiconductors,")
    print("and gorilla habitats are constantly being developed.")
    print("\nWhat would be the most prudent way to address this issue? \n")

    print("If you have any ideas, please send them to echo43@sva.edu via email.")
    print("I will develop Game Season 2 that can convey these related messages. ")
    print("Sustaining the natural environment is crucial not only for animals but also for humans.\n")



def main():
    imgs.StartGame("title")

    intro()


main()
