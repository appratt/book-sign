# This clears the terminal window to give a nice, clean space for writing.
import os
import datetime
os.system('clear')


print "  __    __  __ __   ____  ______      ____  __  ___ ___      ____     ___   ____  ___    ____  ____    ____ \n"
print " |  T__T  T|  T  T /    T|      T    l    jT  ||   T   T    |    \   /  _] /    T|   \  l    j|    \  /    T\n"
print " |  |  |  ||  l  |Y  o  ||      |     |  T l_ || _   _ |    |  D  ) /  [_ Y  o  ||    \  |  T |  _  YY   __j\n"
print " |  |  |  ||  _  ||     |l_j  l_j     |  |   \l|  \_/  |    |    / Y    _]|     ||  D  Y |  | |  |  ||  T  |\n"
print " l  `  '  !|  |  ||  _  |  |  |       |  |     |   |   |    |    \ |   [_ |  _  ||     | |  | |  |  ||  l_ |\n"
print "  \      / |  |  ||  |  |  |  |       j  l     |   |   |    |  .  Y|     T|  |  ||     | j  l |  |  ||     |\n"
print "   \_/\_/  l__j__jl__j__j  l__j      |____j    l___j___j    l__j\_jl_____jl__j__jl_____j|____jl__j__jl___,_j\n"

print "This program will allow you to display the title & author of the book you are reading.\n"
print "In this version, there are two modes:\n"
print ".\n"
print "Type '1' for manual mode. In manual mode, you will type in the book title and author.\n"




# ask for a title
print "Do you have a title for the idea you'd like to catch?"
title = raw_input("Title: ")

print title

# ask for a sentence 
idea = raw_input("Write the idea you want to catch:\n")

print idea

# create a new file with the name
filename = datetime.datetime.now().strftime('%Y-%m-%d') + '.txt'


# write the text to the file
print "Writing the file..."
target = open(filename, 'w')

filecontent = title  + "\n" + "\n" + idea 
target.write(filecontent)

# obvi.
print "And finally, we close it."
target.close()


# close the file
