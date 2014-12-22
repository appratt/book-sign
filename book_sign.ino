// include the library code:
#include <LiquidCrystal.h>
#include <Wire.h>
 
// pin assignments for RGB LCD control
#define REDLIGHT 3
#define GREENLIGHT 5
#define BLUELIGHT 6

String inData; // Buffer to store incoming commands from serial port
String title;
String author;
//int brightness = 255; // intitial brightness for LCD


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
  pinMode(GREENLIGHT, 100);

}

void loop() {
  
  
  // next three lines needs revision
  // would be better to test the length of the inData to see if longer than 16 chars
  //if it is longer, then lcd.autoscroll() else, lcd.noAutoscroll
  lcd.autoscroll();
  lcd.setCursor(0, 0);
  lcd.print(title);
  
  lcd.setCursor(0, 1);
  lcd.print(author);
  
  delay(1000);
  
  while (Serial.available() > 0){
        char recieved = Serial.read();
        
        // in order to get title and author separately, probably need to define another special char
        // for the string sent from the Python script
        // then will have to split the string and print one part on (0,0) and another on (0,1)
        
        if (recieved != '*' && recieved !='\n'){
          inData += recieved;
          inData = title;
          inData = '\0';
          Serial.print(title);
          Serial.print(recieved);
          
        }
        
        if (recieved != '\n'){
          inData += recieved;
          inData = author;
          Serial.print(author);
        }
        
        // want to try and split into two variables: title and author, using a special char...

        // Process message when new line character is recieved
        if (recieved == '\n')
        {
            Serial.print("Arduino Received: ");
            //Serial.print(inData);
            //Serial.print(title);
            //Serial.print(author);
            lcd.clear();
            
        }
    }
}

