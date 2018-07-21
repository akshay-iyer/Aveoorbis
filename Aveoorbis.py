## import the package for enabling serial communication 
import serial

## import package for string operations
import string

## import OS package for enabling operations like playing of songs and videos 
import os

## import Raspberry Pi's GPIO package for GPIO operations 
import RPi.GPIO as GPIO

## import time package to enable delay operations 
from time import sleep

## Setting the GPIO in the GPIO.Board mode
GPIO.setmode(GPIO.BOARD)

## Setting up pins 7,11,13,15 as input pins to receive inputs from the RFID sensors
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)

## Enabling serial UART communication between the RFID sensors and Raspberry Pi
ser=serial.Serial('/dev/ttyAMA0',9600,8,'N',1)

## Setting the file with user inputs as the inputFile
inputFile=open('doc.txt','r')

## Reading user preferences for song, movie, book and shelf from the input file 
songName       = inputFile.readline()
videoName      = inputFile.readline()
bookName       = inputFile.readline()
shelfName      = inputFile.readline()

## Concatenating the input names
songNameShort  = songName.strip()
videoNameShort = videoName.strip()
bookNameShort  = bookName.strip()
shelfNameShort = shelfName.strip()

## Appending the correct file name extensions to the song name and the video name
songNameFull   ='%s.mp3' % songNameShort
videoNameFull  ='%s.mp4' % videoNameShort

## Running an infinite loop
while True:
    
    ## Checking if the user is near the Music Player
	if(GPIO.input(11)==0):
	
	## Yes: Playing the song which the user wants 
        os.system('mpg321 '+p11)
    
	## Checking if the user is near the Music Player
	elif(GPIO.input(7)==0):
        
	## Yes: Playing the movie which the user wants 	
		os.system('omxplayer '+p22)
   
    ## Checking if the user is near the book shelf
    elif(GPIO.input(13)==0):
        
		## Checking if the user has chosen to read Motivational Bestsellers
		if(bookNameShort == "motivational bestsellers"):        
		## Send the command '1' to the microcontroller which corresponds to opening the shelf containing Motivational Bestsellers
			ser.write('1')
    
		## Checking if the user has chosen to read Mystery/Fiction
		elif(bookNameShort == "mystery/fiction"):
		## Send the command '2' to the microcontroller which corresponds to opening the shelf containing Mystery/Fiction
			ser.write('2')
    
		## Checking if the user has chosen to read Children's Books
        elif(bookNameShort == "children's books"):
		## Send the command '3' to the microcontroller which corresponds to opening the shelf containing Children's Books
			ser.write('3')
            		
		## Checking if the user has chosen to read Magazines
        elif(bookNameShort == "magazines"):
		## Send the command '4' to the microcontroller which corresponds to opening the shelf containing Magazines
			ser.write('4')
    
		## Manually induced delay of 400ms
        sleep(0.4)
        string=(ser.read(1))
	
	## Checking if the user is near the food shelf
    elif(GPIO.input(15)==0):
        
		## Checking if the user has chosen to have chocolates
		if(d=="chocolates"):
        ## Send the command '5' to the microcontroller which corresponds to opening the shelf containing chocolates
			ser.write('5')
            
		## Checking if the user has chosen to have soft drinks
		elif(d=="soft drinks"):
        ## Send the command '6' to the microcontroller which corresponds to opening the shelf containing soft drinks
			ser.write('6')
        
		## Checking if the user has chosen to have ready-to-eat food
		elif(d=="ready to eat"):
        ## Send the command '7' to the microcontroller which corresponds to opening the shelf containing ready-to-eat food
			ser.write('7')
        
		## Manually induced delay of 400ms		
        sleep(0.4)
        string=(ser.read(1))
        
            
        

