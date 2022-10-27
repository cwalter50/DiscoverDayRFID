// used this library for rfid.... https://github.com/ArcaEgeCengiz/RFID
// used this article to get it to work with the servo... just adjusted for LED
// Found at this article... https://create.arduino.cc/projecthub/Arca_Ege/arduino-rfid-servo-box-4361f1

#include <SPI.h>
#include <RFID.h>

RFID rfid(10, 9);

boolean card;
int in1 = 5;

void setup()
{

  Serial.begin(9600);
  SPI.begin();
  rfid.init();

 delay(3000); // sanity delay
   pinMode(in1, OUTPUT);
   digitalWrite(in1, HIGH);

}


void loop()
{
 if (rfid.isCard())
  {
      Serial.println("Found a Card");
      digitalWrite(in1, LOW);
      delay(5000);

      rfid.halt();
  }
  else
  {
    digitalWrite(in1, HIGH);
  }
  
}  
