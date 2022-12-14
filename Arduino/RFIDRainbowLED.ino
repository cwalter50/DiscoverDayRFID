// used this library for rfid.... https://github.com/ArcaEgeCengiz/RFID
// used this article to get it to work with the servo... just adjusted for LED
// Found at this article... https://create.arduino.cc/projecthub/Arca_Ege/arduino-rfid-servo-box-4361f1

#include <FastLED.h>
#include <SPI.h>
#include <RFID.h>


RFID rfid(10, 9);

boolean card;

#define LED_PIN     3
#define COLOR_ORDER GRB
#define CHIPSET     WS2811
#define NUM_LEDS    60

#define BRIGHTNESS  100
#define FRAMES_PER_SECOND 60

CRGB leds[NUM_LEDS];

void setup()
{

  Serial.begin(9600);
  SPI.begin();
  rfid.init();

 delay(3000); // sanity delay
  FastLED.addLeds<CHIPSET, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
  FastLED.setBrightness( BRIGHTNESS );
  
Serial.println("Setup Complete");
}


void loop()
{

  if (rfid.isCard())
  {
    
      Serial.println("Found a Card");
      lightCycle();

      rfid.halt();
  }
  else
  {
    // turn everything black
    for (int i = 0; i < NUM_LEDS; i++) {

          leds[i] = CRGB(0, 0, 0); // this is black RGB
               // leds[i] = CRGB::Red;
     }

      FastLED.show();
  }


}

void lightCycle()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    if (i%7==0)
    {
      leds[i] = CRGB::Red;
    }
    else if (i%7==1)
    {
      leds[i] = CRGB::Orange;
    }
    else if (i%7==2)
    {
      leds[i] = CRGB::Yellow;
    }
    else if (i%7==3)
    {
      leds[i] = CRGB::Green;
    }
    else if (i%7==4)
    {
      leds[i] = CRGB::Blue;
    }
    else if (i%7==5)
    {
      leds[i] = CRGB::Purple;
    }
    else if (i%7==6)
    {
      leds[i] = CRGB::White;
    }
    else
    {
      // this should never happen....
      leds[i] = CRGB::Black;
    }
   
   
    FastLED.show();

    FastLED.delay(30);
  }

  for (int i = NUM_LEDS-1; i >= 0; i--)
  {
    leds[i] = CRGB::Black;
    FastLED.show();
    FastLED.delay(30);
  }

  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = CRGB::Black;
  }

  FastLED.show();
  delay(1000);
  //  for (int i = 0; i < NUM_LEDS; i++) {
//
//    leds[i] = CRGB(255, 255, 255); // this is white RGB
//    leds[i] = CRGB(0, 0, 0); // this is black RGB
//          leds[i] = CRGB::Red;
//  }
//
//  FastLED.show();
//
//  delay(1000);
}
