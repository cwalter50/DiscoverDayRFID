// used this library for rfid.... https://github.com/ArcaEgeCengiz/RFID
// used this article to get it to work with the servo... just adjusted for LED
// Found at this article... https://create.arduino.cc/projecthub/Arca_Ege/arduino-rfid-servo-box-4361f1


#include <Servo.h>
#include <SPI.h>
#include <RFID.h>

RFID rfid(10, 9);

Servo myservo;
boolean card;

void setup()
{

  Serial.begin(9600);
  SPI.begin();
  rfid.init();

    myservo.attach(3);
    myservo.write(100);
//  delay(3000); // sanity delay

  Serial.println("Ready to Go!");
}

void loop()
{

  if (rfid.isCard())
  {
   
    // We Found RFID...  write code here.
    Serial.println("Found Card");
//    myservo.attach(3);
    myservo.write(110); // 110 is degrees
    delay(2000);
    myservo.write(20); // this is in degress

//    myservo.detach(); // tried to attach then detach servo to stop humming. It was not neccessary.
   
    rfid.halt();
  }
  else
    {
      Serial.println("No Card");

    }
}
