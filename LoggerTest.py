#!/usr/bin/env python2
import RPi.GPIO as GPIO
from Logger import Logger

"""
Test for the Logger Class. A circuit is made with a push button (initially pulled up) and an LED.
A message is recorded to the log file when a button is pressed, and when an LED is turned on or off.
Author: Katelyn Lam			
Date: Feb 2021
"""
buttonPin = 11 #pin location of switch
ledPin = 12 #pin location of LED
ledState = False #state of LED on or off

#configures board: INPUT for button (pulled up) and OUTPUT for LED
def setup():
    print ("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #initializes buttonPin as input with initial value 3.3V


def buttonEvent():
    Logger.writeLog("Button pressed")
    startTime = time.time()
    
	#reverses state of LED when buttonEvent is called (turns on when 
	global ledState
    ledState = not ledState; 
    if ledState == True:
        message = "Turn on LED..."
    else:
        message = "Turn off LED..."
    GPIO.output(ledPin,ledState)
    Logger.writeLog(message + " Elapsed time: " + str(time.time()-startTime) #records time it takes for LED to turn on/off from when the button is pressed

def loop():
    #adds event to button with debounce of 300ms
	GPIO.add_event_detect(buttonPin,GPIO.FALLING, callback = buttonEvent, bouncetime = 300) 
    while True:
        pass

#disables board, first turning off the LED		
def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()



#main body of program
#detects for button press and turns on/off LEDs until a key is pressed
if __name__ == "__main__":
    setup()
    try:
        loop()                     
    except KeyboardInterrupt:
        destroy()
        
