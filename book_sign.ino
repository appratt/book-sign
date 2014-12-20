// include the library code:
#include <LiquidCrystal.h>
#include <Wire.h>
 
#define REDLIGHT 3
#define GREENLIGHT 5
#define BLUELIGHT 6

// Buffer to store incoming commands from serial port
String inData;

// initialize the library with the numbers of the interface pins
// pin assignments form here: https://learn.adafruit.com/character-lcds/using-a-character-lcd
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  // set speed for serial communication
  Serial.begin(9600);
  
  // this is morefor debugging
  Serial.println("Waiting for book\n");
  
  // intial screen reads
  lcd.print("Waiting for book");

  // RGB backlight mode  
  pinMode(GREENLIGHT, HIGH);

}

void loop() {
  lcd.setCursor(0, 0);
  
  // next three lines needs revision
  // would be better to test the length of the inData to see if longer than 16 chars
  //if it is longer, then lcd.autoscroll() else, lcd.noAutoscroll
  lcd.autoscroll();
  lcd.print(inData);
  delay(1000);
  
  while (Serial.available() > 0){
        char recieved = Serial.read();
        
        // in order to get title and author separately, probably need to define another special char
        // for the string sent from the Python script
        // then will have to split the string and print one part on (0,0) and another on (0,1)
        
        if (recieved != '\n'){
          inData += recieved;
        }

        // Process message when new line character is recieved
        if (recieved == '\n')
        {
            Serial.print("Arduino Received: ");
            Serial.print(inData);
            lcd.clear();
            
            //inData = ""; // Clear recieved buffer.
            // ^ this line screws up the functionality, but i don't get why...
        }
    }
}

