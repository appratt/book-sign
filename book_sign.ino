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
int delimiterIndex; // use * as delimiter
int secondDelimiterIndex;
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
  
  lcd.noAutoscroll();
  lcd.setCursor(0, 1);
  lcd.print(author);
  
  delay(1800);
      
  //lcd.setCursor(0, 1);
    
  while (Serial.available() > 0){
        char recieved = Serial.read();
        
        // in order to get title and author separately, probably need to define another special char
        // for the string sent from the Python script
        // then will have to split the string and print one part on (0,0) and another on (0,1)
        
        if (recieved !='|'){
          inData += recieved;
        }
        
        // want to try and split into two variables: title and author, using a special char...

        // Process message when new line character is recieved
        if (recieved == '|'){
          
          // for explanation of the code below, see: http://stackoverflow.com/questions/11068450/arduino-c-language-parsing-string-with-delimiter-input-through-serial-interfa
          // use the indexOf function to count to the index points within a string and find a delimiter
          delimiterIndex = inData.indexOf('*');
          secondDelimiterIndex = inData.indexOf('*', delimiterIndex+1);
          // select substrings of a string using the index found with the delimiter 
          title = inData.substring(0, delimiterIndex); 
          author = inData.substring(delimiterIndex+1, secondDelimiterIndex);
          Serial.print("BOOK TITLE: ");
          //Serial.print(inData);
          Serial.print(title);
          Serial.print("BOOK AUTHOR: ");
          Serial.print(author);
          lcd.clear();
            
        }
    }
}

