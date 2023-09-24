
import os
from playsound import playsound # pip3 install playsound

# Get the path of the sound file
currentDirectory = os.getcwd()
filepath = os.path.join(currentDirectory, 'sounds/Sound02.wav')

# make sure the file exists
#print(filepath)

# play the sound

def StartGame(scene):
    if(scene == "title"):

        print(' _______                                                __    __                          ')
        print('|       \                                              |  \  |  \                         ')
        print('| $$$$$$$\  ______   ______  __     __   ______        | $$\ | $$  ______   __   __   _ _ ')
        print('| $$__/ $$ /      \ |      \|  \   /  \ /      \       | $$$\| $$ /      \ |  \ |  \ |  \ ')
        print('| $$    $$|  $$$$$$\ \$$$$$$\\$$\ /  $$|  $$$$$$\      | $$$$\ $$|  $$$$$$\| $$ | $$ | $$ ')
        print('| $$$$$$$\| $$   \$$/      $$ \$$\  $$ | $$    $$      | $$\$$ $$| $$    $$| $$ | $$ | $$ ')
        print('| $$__/ $$| $$     |  $$$$$$$  \$$ $$  | $$$$$$$$      | $$ \$$$$| $$$$$$$$| $$_/ $$_/ $$ ')
        print('| $$    $$| $$      \$$    $$   \$$$    \$$     \      | $$  \$$$ \$$     \ \$$   $$   $$ ')
        print(' \$$$$$$$  \$$       \$$$$$$$    \$      \$$$$$$$       \$$   \$$  \$$$$$$$  \$$$$$\$$$$  ')
        print('                                                                                          ')
        print(' __       __                      __        __ ')
        print('|  \  _  |  \                    |  \      |  \ ')
        print('| $$ / \ | $$  ______    ______  | $$  ____| $$')
        print('| $$/  $\| $$ /      \  /      \ | $$ /      $$')
        print('| $$  $$$\ $$|  $$$$$$\|  $$$$$$\| $$|  $$$$$$$')
        print('| $$ $$\$$\$$| $$  | $$| $$   \$$| $$| $$  | $$')
        print('| $$$$  \$$$$| $$__/ $$| $$      | $$| $$__| $$')
        print('| $$$    \$$$ \$$    $$| $$      | $$ \$$    $$')
        print(' \$$      \$$  \$$$$$$  \$$       \$$  \$$$$$$$')
        playsound(filepath)

    
    if(scene == "Intro"):
        print("\n hello! Nice to meet you 😎 \n ")

    if(scene == "Crushing"):
        print("    ___(                        )")
        print("   (                          _) ")
        print("   (_                       __)) ")
        print("    ((                _____)     ")
        print("      (_________)----'           ")
        print("        _/  /                    ")
        print("      /  _/                      ")
        print("    _/  /                        ")
        print("  / __/                          ")
        print("    _/ /                         ")
        print("   /__/                          ")
        print("   //                            ")
        print("  /'^)                           ")

    if(scene == "gorilla"):
        print("         .'`''.      ")
        print("     .-./ _=_ \.-.   ")
        print("    {  (,(oYo),) }}  ")
        print("    {{ |   ^   |} }  ")
        print("    { { \(---)/  }}  ")
        print("    {{  }'-=-'{ } }  ")
        print("    { { }._:_.{  }}  ")
        print("    {{  } -:- { } }  ")
        print("    {_{ }`===`{  _}  ")
        print("    ((((\)     (/))))")

    if(scene == "sick"):
        print("           __    EEEK!")
        print("      /  \   ~~|~~    ")
        print("     (|00|)    |      ")
        print("      (==)  --/       ")
        print("    ___||___          ")
        print("   / _ .. _ \         ")
        print("  //  |  |  \\        ")
        print(" //   |  |   \\       ")
        print(" ||  / /\ \  ||       ") 
        print("_|| _| || |_ ||_      ")
        print("\|||___||___|||/      ")
