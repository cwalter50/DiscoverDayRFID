// used this library for rfid.... https://github.com/ArcaEgeCengiz/RFID
// used this article to get it to work with the servo... just adjusted for LED
// Found at this article... https://create.arduino.cc/projecthub/Arca_Ege/arduino-rfid-servo-box-4361f1


#include <SPI.h>
#include <RFID.h>

#include <Servo.h>

Servo myservo;

RFID rfid(10, 9);

boolean card;

void setup() {


  Serial.begin(9600);
  SPI.begin();
  rfid.init();
  
 // myservo.attach(6);

Serial.println("Connecting");

 delay(1000); // sanity delay
  

}

void loop() {
 if (rfid.isCard())
  {
      Serial.println("Found a Card");
  
  // MAKE SURE STRING is TIGHTISH with the TAPE on FOSTERS HEAD
      myservo.attach(6);
      // continuos servo: write 90: Dont move. Write 180 turns Left or Right, Write 0 turns the other way. THe delay is how long you turn for.
       myservo.write(120); 
       delay(725);

      myservo.write(90);
      delay(1000);
       
       myservo.write(60);
       delay(615);
      
    
     // rfid.halt();       
      
      myservo.detach();
  }
  else
  {
    // stop it from moving
    myservo.detach();
     }

}