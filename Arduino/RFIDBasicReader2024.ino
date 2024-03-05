// We started using this for the RFID programs in the spring 2024. The program works with the RFID-RC522 reader.
/* 
 * --------------------------------------------------------------------------------------------------------------------
 * Typical pin layout used:
 * -----------------------------------------------------------------------------------------
 * MFRC522         Arduino 
 * Reader/PCD      Uno/101 
 * Signal          Pin 
 * -----------------------------------------------------------------------------------------
 * RST/Reset RST   9 
 * SPI SDA(SS)     10 
 * SPI MOSI        11 / ICSP-4 
 * SPI MISO        12 / ICSP-1 
 * SPI SCK         13 / ICSP-3 
 * SPI GND         GND
 * SPI 3.3V        3.3V
 * More pin layouts for other boards can be found here: https://github.com/miguelbalboa/rfid#pin-layout
 */
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the RFID class
int count = 0;

void setup() {

   Serial.begin(9600);
   SPI.begin(); // Init SPI bus
   rfid.PCD_Init(); // Init MFRC522 
   Serial.println("RFID RC522 is connected");

}

void loop() {

   // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
   if ( ! rfid.PICC_IsNewCardPresent())
      return;

   // Verify if the NUID has been readed
   if ( ! rfid.PICC_ReadCardSerial())
      return;

   // If you get to this line of code it means you found a card.....
   count++;
   Serial.print("Found a card ");
   Serial.println(count);

   // Halt PICC
   rfid.PICC_HaltA();

   // Stop encryption on PCD
   rfid.PCD_StopCrypto1();
}