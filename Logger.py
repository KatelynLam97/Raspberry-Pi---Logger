import os
import datetime

"""
A logger class writes to a log file with the current date, creating one if none exists.
After an action is performed, a line is written to the log file with the current time and a description 
of the action. This same line is outputted.
Author: Katelyn Lam			
Date: Feb 2021
"""
class Logger(object):

	#writes to a log file
    def writeLog(message):
        
        #get current date and time of program run
        runDate = datetime.data.today()
        fileName = runDate.strftime()
        currentTime = datetime.time()

        #record current time in HH:MM:SS:uuu where H is the hour, m is minutes,
        #s is seconds, and uuu is milliseconds (converted from microseconds)
        #adds message to same line as time
        microseconds = currentTime.strftime("%f"))/1000
        stringTime = currentTime.strftime("%H:%M:%S")+str(microseconds)+ " \t " + message + " \r\n" 

        #opens log file named after date or program run, or creates a new log file
        #if none exists. Write message to log file, and close.
        logFile = open(fileName,"a")
        logFile.write(stringTime)
        logFile.close()
        print(stringTime)
        
        
