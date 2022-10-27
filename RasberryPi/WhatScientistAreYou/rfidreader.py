
# Simple Python program to test RFID reader.  
# to Run navigate to the folder in terminal and type "sudo python rfidreader.py"

from guizero import App, Text, PushButton
import RPi.GPIO as GPIO
import sys
import random

sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
scientists = ["chemist", "biologist", "computer scientist", "rocket scientist"]
app = App(title = "Which scientist are you?", width = 800, height = 600)
whichScientist = Text(app, text = "I am a...", size = 40, font = "Arial", color = "darkGray")
def randomScientist():
    whichScientist.value = "I am a " + random.choice(scientists)

scientistButton = PushButton(app, command = randomScientist, text = "Tell me!")
app.display()
try:
    id, text = reader.read()
    print(id)
    print(text)

    

finally:
    GPIO.cleanup()
