import random


# for RFID reader 
import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

# for reading RFID reader
reader = SimpleMFRC522()

from guizero import App, Text, TextBox, PushButton, Picture


def checkRFidTag():
    try:
        #while True:
        
        id, text = reader.read()
        print(id)
        print(text)
        getRandomScientist();

    finally:
        GPIO.cleanup()


# array of scientists
sciList = ["Chemist", "Biologist", "Computer Scientist", "Physicist"]

# Create the App 
app = App(title="ScientistPicker",width=800, height=600)

#add widgets here

# first parameter in Text tells us where to put the text
welcomeMessage = Text(app, text="What kind of Scientist are you?", size=40, font="Arial", color="black")



#myName = TextBox(app, width=30)

#This is a function. Order is important. Func must be written before updateText
def getRandomScientist():
    
    #welcomeMessage.value = "Hello " + myName.value
    welcomeMessage.value = random.choice(sciList)
    welcomeMessaage.focus()
    

updateText = PushButton(app, command=getRandomScientist, text="Display my name")
print("Hold a tag near the reader")
rfidStatus = Text(app, text="---")
rfidStatus.repeat(1000, checkRFidTag)

#pictures must be in .gif format, but animated gifs will only appear as stills.

#groot = Picture(app, image="groot.gif")

app.display()



