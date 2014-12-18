import serial # if you have not already done so
import time


PORT = '/dev/tty.usbmodem1421'

# Open a connection to the serial port.  This will reset the Arduino
ser = serial.Serial('/dev/tty.usbmodem1421', 9600)
# Must given Arduino time to rest.
# Any time less than this does not seem to work...
time.sleep(2)


# in order to get title and author separately, probably need to define another special char
# for the string sent from the Python script
# then will have to split the string and print one part on (0,0) and another on (0,1)
        
ser.write('Fellowship\n')



