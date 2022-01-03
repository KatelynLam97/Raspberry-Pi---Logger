# Raspberry-Pi---Logger
A logger class that records an action to a text file after it is executed.

The logger class contains a static method writeLog() that opens a log file with the name of the current date. The current time and a description of a performed action is recorded, and the file is closed when recording is completed.

A class to test the logger is provided. A push-button (pulled up) is used to control a red LED on the Raspberry Pi (see LoggerTest_Schematic.pdf). Logger writes the following actions to a text file:
 - When a button is pressed
 - When the LED turns on or off
 - The elapsed time from the button press to when the LED turns on or off
 
 The program was tested on a Raspberry Pi 4B and uses the Python RPi.GPIO library.
 
 
