# this verion exits b/c i doni't understand how to roll back changes in git

import os
import serial
import time
#import datetime
os.system('clear') # This clears the terminal window to give a nice, clean space for writing.

# setting values for global variable in case needed for debugging
title = 'book title'
author = 'book author'

def get_title():
	# ask for a title
	global title
	print "What is the title of your book?"
	title = raw_input("Title: ")
	title = title + "*"

	print title


def get_author():
	# ask for a author
	global author
	print "Who is the author of your book?" 
	author = raw_input("Author:\n")

	print author + "\n"


def send_to_serial():

	# combine the title and the author together
	bookInfo = title + author

	PORT = '/dev/tty.usbmodem1411'

	# Open a connection to the serial port.  This will reset the Arduino
	ser = serial.Serial('/dev/tty.usbmodem1411', 9600)
	# Must given Arduino time to rest.
	# Any time less than this does not seem to work...
	time.sleep(2)

	# in order to get title and author separately, probably need to define another special char
	# for the string sent from the Python script
	# then will have to split the string and print one part on (0,0) and another on (0,1)
	
	# write the combined title and author to the serial output
	ser.write(bookInfo)


def print_howto():
	print "This program will allow you to display the title & author of the book you are reading.\n"
	print "In future versions there will be two modes:"
	print "Manual mode will allow you to type in the title of the book directly."
	print "Goodreads mode will pull your Goodreads currently reading list and use that display book titles.\n"
	print "...At the moment, only manual mode is functional.\n"


print_howto()
get_title()
get_author()
send_to_serial()











#print "  __    __  __ __   ____  ______      ____  __  ___ ___      ____     ___   ____  ___    ____  ____    ____ "
#print " |  T__T  T|  T  T /    T|      T    l    jT  ||   T   T    |    \   /  _] /    T|   \  l    j|    \  /    T"
#print " |  |  |  ||  l  |Y  o  ||      |     |  T l_ || _   _ |    |  D  ) /  [_ Y  o  ||    \  |  T |  _  YY   __j"
#print " |  |  |  ||  _  ||     |l_j  l_j     |  |   \l|  \_/  |    |    / Y    _]|     ||  D  Y |  | |  |  ||  T  |"
#print " l  `  '  !|  |  ||  _  |  |  |       |  |     |   |   |    |    \ |   [_ |  _  ||     | |  | |  |  ||  l_ |"
#print "  \      / |  |  ||  |  |  |  |       j  l     |   |   |    |  .  Y|     T|  |  ||     | j  l |  |  ||     |"
#print "   \_/\_/  l__j__jl__j__j  l__j      |____j    l___j___j    l__j\_jl_____jl__j__jl_____j|____jl__j__jl___,_j\n"









