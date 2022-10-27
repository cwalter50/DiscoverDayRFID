#Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
#[GCC 6.3.0 20170516] on linux
#Type "copyright", "credits" or "license()" for more information.
#>>> 
import random

from guizero import App, Text, TextBox, PushButton, Picture

# Custom Class of Scientist. Will be used to connect name, description, and image
class Scientist:
  def __init__(self, name, description, image):
    self.name = name
    self.description = description
    self.image = image



# array of scientists
sciList = [Scientist("Chemist", "A chemist searches for new knowledge about chemicals\n and uses it to improve the way we live.", "chemist.gif"),#fix here
           Scientist("Biologist", "Biologists study organisms and plant life to learn more \nabout their composition, behaviors, habitats, and how\n they interact with other organisms and their environment.", "Biology.gif"),
           Scientist("Computer Scientist", "Computer scientists design and analyze algorithms to solve programs \nand study the performance of computer hardware and software.", "CS.gif") ,
           Scientist("Agronomist","An agronomist specializes in soil and crops.","agronomist.jpeg"),
           Scientist("Astronomer","An astronomer studies stars, planets and galaxies.","groot.gif"),
           Scientist("Botanist","A botanist specializes in plants.","groot.gif"),
           Scientist("Cytologist","A cytologist specializes in the study of cells.","groot.gif"),
           Scientist("Epidemiologist","An epidemiologist studies the spread of diseases.","groot.gif"),
           Scientist("Ethologist","An ethologist studies animal behavior.","groot.gif"),
           Scientist("Geneticist","A geneticist studies how traits are inherited.","groot.gif"),
           Scientist("Geologist","A geologist specializes in the history of Earth.","groot.gif"),
           Scientist("Geographer","A geographer studies Earth's surface.","groot.gif"),
           Scientist("Marine Biologist","A marine biologist studies ocean plants and animals.","groot.gif"),
           Scientist("Meteorologist","A meteorologist studies weather and climate.","groot.gif"),
           Scientist("Microbiologist","A microbiologist studies microscopic plants and animals.","microbiologist.jpeg"),
           Scientist("Paleontologist","A paleontologist specializes in fossils.","groot.gif"),
           Scientist("Physicist","A physicist studies matter, energy, and how they are related.","groot.gif"),
           Scientist("Seismologist","A seismologist studies earthquakes.","groot.gif"),
           Scientist("Anthropologist (an(t) thra pä lə jist)","A scientist who studies societies and cultures","groot.gif"),
           Scientist("Archaeologist"," A scientist who studies human history, particularly the culture of\nhistoric and prehistoric people, through discovery and exploration of remains,\nstructures and writings.","groot.gif"),
           Scientist("Climatologist","A scientist who studies climate change, climate variation, and the\neffects of climate on Earth.","groot.gif"),
           Scientist("Dendrologist","A scientist who studies trees.","groot.gif"),
           Scientist("Engineer","A person who studies, designs, and/or builds complicated products,\nmachines, systems, or structures.","groot.gif"),
           Scientist("Entomologist (en tə mä lə jist)","A scientist who studies insects.","groot.gif"),
           Scientist("Forester","A scientist who studies forests, or is skilled in planting, managing, or\ncaring for trees.","groot.gif"),
           Scientist("Hydrologist","A scientist who studies water and the water cycle.","groot.gif"),
           Scientist("Ornithologist (ȯr nə thä lə jist)","A person who studies birds","groot.gif"),
           Scientist("Social Scientist","A scientist who studies the values, opinions, beliefs, attitudes, and\nactions of individuals and groups of people.","groot.gif"),
           Scientist("Statistician","A scientist who uses statistical tools to design data collection plans,\nanalyze data, graph data, and help solve real-world problems in business,\nengineering, the sciences, or other fields.","groot.gif"),
           Scientist("Zoologist"," A scientist who studies animal and animal life.","groot.gif"),
           Scientist("Actuary","An actuary is a business professional who analyzes the financial\n consequences of risk.","groot.gif"),
           Scientist("Mathematician","help solve real-world problems by analyzing data and applying\n mathematical techniques","groot.gif"),
           Scientist("Cryptographer","A Cryptographer develops algorithms, ciphers and security systems to\n encrypt sensitive information.","groot.gif"),
        
           
           Scientist("","","")]

#sciList = ["Chemist", "Biologist", "Computer Scientist"]

# Create the App 
app = App(title="ScientistPicker",width= 800, height = 600 )

#add widgets here


# first parameter in Text tells us where to put the text
welcomeMessage = Text(app, text="What kind of Scientist are you?", size=40, font="Arial", color="darkGray")


#myName = TextBox(app, width=30)

#This is a function. Order is important. Func must be written before updateText
def getRandomScientist():
    
    #welcomeMessage.value = "Hello " + myName.value
    theSci = random.choice(sciList)
    responseMessage.value = theSci.name
    descriptionMessage.value = theSci.description
    groot.image = theSci.image
    
    

updateText = PushButton(app, command=getRandomScientist, text="Display Scientist")




responseMessage = Text(app, text="", size=30, font="Arial", color="black")
descriptionMessage = Text(app, text = "", size = 20, font="Arial", color ="darkGray")



#pictures must be in .gif format, but animated gifs will only appear as stills.
#to make sure you can scale images, you have to add the following line in terminal 
#On rasberry pi  "sudo pip3 install guizero[images]"
#On windows or mac "pip3 install guizero[images]"
groot = Picture(app, image="groot.gif", width=250, height = 250)

app.display()
