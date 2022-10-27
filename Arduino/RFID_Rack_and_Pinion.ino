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


 delay(1000); // sanity delay
  

}

void loop() {
 if (rfid.isCard())
  {
      Serial.println("Found a Card");
  
  
  myservo.attach(6);

       myservo.write(0);
       delay(2200);

      myservo.write(90);
      delay(1000);
       
       myservo.write(180);
       delay(2000);
      
    
     // rfid.halt();       
      
      myservo.detach();
  }
  else
  {
    // stop it from moving
    myservo.detach();
     }

}
