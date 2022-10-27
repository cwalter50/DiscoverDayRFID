
import random

# for RFID reader 
import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/MFRC522-python')
from mfrc522 import SimpleMFRC522

# for reading RFID reader
reader = SimpleMFRC522()

from guizero import App, Text, TextBox, PushButton, Picture

# Custom Class of Scientist. Will be used to connect name, description, and image
class Scientist:
  def __init__(self, name, description, image):
    self.name = name
    self.description = description
    self.image = image
    




# array of scientists
sciList = [Scientist("Chemist", "A chemist searches for new knowledge about chemicals\n and uses it to improve the way we live.", "chemists.gif"),
           Scientist("Biologist", "Biologists study organisms and plant life to learn more \nabout their composition, behaviors, habitats, and how\n they interact with other organisms and their environment.", "biologists.gif"),
           Scientist("Computer Scientist", "Computer scientists design and analyze algorithms to solve programs \nand study the performance of computer hardware and software.", "compsci.gif") ,
           Scientist("Agronomist","An agronomist specializes in soil and crops.","agronomist.jpeg"),
           Scientist("Astronomer","An astronomer studies stars, planets and galaxies.","milkyway.jpeg"),
           Scientist("Botanist","A botanist specializes in plants.","botanist.jpeg"),
           Scientist("Cytologist","A cytologist specializes in the study of cells.","plantcell.jpeg"),
           Scientist("Epidemiologist","An epidemiologist studies the spread of diseases.","epidemologist.jpeg"),
           Scientist("Ethologist","An ethologist studies animal behavior.","ethology.jpeg"),
           Scientist("Geneticist","A geneticist studies how traits are inherited.","DNA.jpeg"),
           Scientist("Geologist","A geologist specializes in the history of Earth.","geologists.jpeg"),
           Scientist("Geographer","A geographer studies Earth's surface.","geographer.jpeg"),
           Scientist("Marine Biologist","A marine biologist studies ocean plants and animals.","marinebiology.jpeg"),
           Scientist("Meteorologist","A meteorologist studies weather and climate.","meteorologist.jpeg"),
           Scientist("Microbiologist","A microbiologist studies microscopic plants and animals.","microbiologist.jpeg"),
           Scientist("Paleontologist","A paleontologist specializes in fossils.","dino.jpeg"),
           Scientist("Physicist","A physicist studies matter, energy, and how they are related.","pendulum.jpeg"),
           Scientist("Seismologist","A seismologist studies earthquakes.","seismograph.jpeg"),
           Scientist("Anthropologist (an(t) thra pä lə jist)","A scientist who studies societies and cultures","anthro.jpeg"),
           Scientist("Archaeologist"," A scientist who studies human history, particularly the culture of\nhistoric and prehistoric people, through discovery and exploration of remains,\nstructures and writings.","archae.jpeg"),
           Scientist("Climatologist","A scientist who studies climate change, climate variation, and the\neffects of climate on Earth.","clima.jpeg"),
           Scientist("Dendrologist","A scientist who studies trees.","dendro.jpeg"),
           Scientist("Engineer","A person who studies, designs, and/or builds complicated products,\nmachines, systems, or structures.","eng.jpeg"),
           Scientist("Entomologist (en tə mä lə jist)","A scientist who studies insects.","ento.jpeg"),
           Scientist("Forester","A scientist who studies forests, or is skilled in planting, managing, or\ncaring for trees.","forester.jpeg"),
           Scientist("Hydrologist","A scientist who studies water and the water cycle.","hydro.jpeg"),
           Scientist("Ornithologist (ȯr nə thä lə jist)","A person who studies birds","bird.jpeg"),
           Scientist("Social Scientist","A scientist who studies the values, opinions, beliefs, attitudes, and\nactions of individuals and groups of people.","social.jpeg"),
           Scientist("Statistician","A scientist who uses statistical tools to design data collection plans,\nanalyze data, graph data, and help solve real-world problems in business,\nengineering, the sciences, or other fields.","stats.jpeg"),
           Scientist("Zoologist"," A scientist who studies animal and animal life.","zoo.jpeg"),
           Scientist("Actuary","An actuary is a business professional who analyzes the financial\n consequences of risk.","actuary.jpeg"),
           Scientist("Mathematician","help solve real-world problems by analyzing data and applying\n mathematical techniques","einstein.jpeg"),
           Scientist("Cryptographer","A Cryptographer develops algorithms, ciphers and security systems to\n encrypt sensitive information.","crypto.jpeg"),
           ]

def checkRFidTag():
    try:
        #while True:
        id, text = reader.read()
        print(id)
        print(text)
        getRandomScientist();

    finally:
        GPIO.cleanup()

#sciList = ["Chemist", "Biologist", "Computer Scientist"]

# Create the App 
app = App(title="ScientistPicker",width= 1820, height = 1100, bg = "lightBlue")


#add widgets here


# first parameter in Text tells us where to put the text
welcomeMessage = Text(app, text="What type of Scientist are you?", size=90, font="Arial", color="black")

#myName = TextBox(app, width=30)

#This is a function. Order is important. Func must be written before updateText
def getRandomScientist():
    
    #welcomeMessage.value = "Hello " + myName.value
    theSci = random.choice(sciList)
    #theSci = sciList[3]
    responseMessage.value = theSci.name
    descriptionMessage.value = theSci.description
    groot.image = theSci.image

  
#updateText = PushButton(app, command=getRandomScientist, text="Display Scientist")






spacer = Text(app, text = " ", size = 55, font = "Arial", color = "black")
responseMessage = Text(app, text="", size=75, font="Arial", color="black")
descriptionMessage = Text(app, text = "", size = 40, font="Arial", color ="white")


# this will call the RFID reader function defined above every 1 second
responseMessage.repeat(500, checkRFidTag)
#pictures must be in .gif format, but animated gifs will only appear as stills.
#to make sure you can scale images, you have to add the following line in terminal 
#On rasberry pi  "sudo pip3 install guizero[images]"
#On windows or mac "pip3 install guizero[images]"
groot = Picture(app, image="DNA.jpeg", width=350, height = 350)
#groot = Picture(app, image="groot.gif")

app.display()
