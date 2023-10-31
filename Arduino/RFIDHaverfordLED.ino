// used this library for rfid.... https://github.com/ArcaEgeCengiz/RFID
// FastLED stopped working in October 2023. Now using this for LED Light Strip.
// https://github.com/adafruit/Adafruit_NeoPixel

// This Program has 5 reds and 5 golds alternating colors

// #include <FastLED.h>
#include <SPI.h>
#include <RFID.h>
#include <Adafruit_NeoPixel.h>
// #ifdef __AVR__
//  #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
// #endif


RFID rfid(10, 9);

boolean card;


// Which pin on the Arduino is connected to the NeoPixels?
// On a Trinket or Gemma we suggest changing this to 1:
#define LED_PIN    6

// How many NeoPixels are attached to the Arduino?
#define LED_COUNT 60

// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
// Argument 1 = Number of pixels in NeoPixel strip
// Argument 2 = Arduino pin number (most are valid)
// Argument 3 = Pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)

void setup()
{

  Serial.begin(9600);
  SPI.begin();
  rfid.init();

  delay(3000); // sanity delay
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)
  
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
    strip.clear();
  }
}

void lightCycle() {
  strip.clear();

  for(int i=0; i<LED_COUNT; i++) {
    if (i%10<5) {
      strip.setPixelColor(i, strip.Color(255,0,0));
    } else {
      strip.setPixelColor(i, strip.Color(255,255,20));
    }
    strip.show();
    delay(20);
  }

    for(int i=LED_COUNT-1; i>=0; i--) {
      strip.setPixelColor(i, strip.Color(0,0,0));
      strip.show();
      delay(20);
    }
    strip.clear();
}
