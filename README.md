book-sign
=========
This is an Arduino project that powers an LCD sign that displays the title & author of a book. It is designed to be used either as a manually-controlled sign with arbitrary text input, or a small program can pull books the user is currently reading from a Goodreads.com list and display one of those.

The project is a combination of:
- an Arduino sketch that controls the LCD display
- a command-line Python program that captures book information and sends it via the PySerial library to the Arduino over a serial connection
- a set of AppleScripts that open the necessary Terminal programs to avoid navigating through the commandline
