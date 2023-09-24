
import os
from playsound import playsound # pip3 install playsound
import random
import sys

# Get the path of the sound file
currentDirectory = os.getcwd()
filepath = os.path.join(currentDirectory, 'sounds/SFX_GET_ITEM_1.wav')

# make sure the file exists
print(filepath)

# play the sound
playsound(filepath)

player = {
    "name": "p1",
    "score": 0,
    "items" : ["milk"],
    "friends" : [],
    "location" : "start"
}

rooms = {
    "room1" : "a forest clearing",
    "room2" : "a forest path",
    "room3" : "an alternate path"
}

#def playOddEven()