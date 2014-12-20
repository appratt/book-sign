# This clears the terminal window to give a nice, clean space for writing.
import os
import datetime
os.system('clear')

# test git

print "  __    __  __ __   ____  ______      ____  __  ___ ___      ____     ___   ____  ___    ____  ____    ____ "
print " |  T__T  T|  T  T /    T|      T    l    jT  ||   T   T    |    \   /  _] /    T|   \  l    j|    \  /    T"
print " |  |  |  ||  l  |Y  o  ||      |     |  T l_ || _   _ |    |  D  ) /  [_ Y  o  ||    \  |  T |  _  YY   __j"
print " |  |  |  ||  _  ||     |l_j  l_j     |  |   \l|  \_/  |    |    / Y    _]|     ||  D  Y |  | |  |  ||  T  |"
print " l  `  '  !|  |  ||  _  |  |  |       |  |     |   |   |    |    \ |   [_ |  _  ||     | |  | |  |  ||  l_ |"
print "  \      / |  |  ||  |  |  |  |       j  l     |   |   |    |  .  Y|     T|  |  ||     | j  l |  |  ||     |"
print "   \_/\_/  l__j__jl__j__j  l__j      |____j    l___j___j    l__j\_jl_____jl__j__jl_____j|____jl__j__jl___,_j\n"

print "This program will allow you to display the title & author of the book you are reading.\n"
print "In future versions there will be two modes:"
print "Manual mode will allow you to type in the title of the book directly."
print "Goodreads mode will pull your Goodreads currently reading list and use that display book titles.\n"
print "At the moment, only manual mode is functional."

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
