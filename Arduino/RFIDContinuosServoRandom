#include <Servo.h>

#include <SPI.h>
#include <RFID.h>


RFID rfid(10, 9);

boolean card;

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position


void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.init();

  delay(3000); // sanity delay
  
  myservo.attach(3);  // attaches the servo on pin 9 to the servo object
}

void loop() {


  if (rfid.isCard())
  {
    
      Serial.println("Found a Card");
      servoRun();

      rfid.halt();
  }
  else
  {
    // No card Found...
    myservo.detach();
  }

}

// Servo will run at full speed for a random amount of time between 2 and 5 seconds
void servoRun() {
  myservo.attach(3);

  int randNum = random(2000, 5000);

 // Servo spins forward at full speed for 1 second.
  myservo.write(180);
  delay(randNum);
  // Servo is stationary for 1 second.
//  myservo.write(90);
//  delay(1000);
//  // Servo spins in reverse at full speed for 1 second.
//  myservo.write(0);
//  delay(1000);
//  // Servo is stationary for 1 second.
//  myservo.write(90);
//  delay(1000);

}
