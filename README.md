# Aveoorbis
Personalising the world around you!

A project that allowed guests to personalize the world around them

Guests enter their media preferences and choice of entertainment and are given RFID chips to be worn around the wrist. The Television and the Music player respond as per the user's request when the user move towards them.

Also, in shopping malls, the user needs to share his shopping list and the corresponding shelves with those items pop out for him when he goes to that section in the store

HOW IT WORKS?:
1. The project is powered by Raspberry Pi, RFID sensors, Atmega 8 microcontroller, motor drivers and DC motors 
2. Raspberry Pi is the used as the central computer which interfaces with the RFID sensors and plays the media of choice
3. The user needs to enter his/her preferences in the input file (doc.txt) 
4. Pi will read the file and know the user preferences 
5. When the user is near the television and swipes his hand containing the RFID band at the RFID receiver, the corresponding pin in the      GPIO board of Raspberry Pi becomes active low
6. Then based on the user's movie preference stated in the input file, Pi plays the movie in the television
7. The other modules for playing songs and opening the shelves work in a similar fashion

HOW TO READ THE CODE:
1. The code file Aveoorbis.py contains four parts:
  i.   Playing the song of the user's choice 
  ii.  Playing the movie of the user's choice
  iii. Opening the shelf with the book the user wants to read
  iv.  Opening the shelf containing the food item which the user wants to eat
2. In each of the parts, the Raspberry Pi first checks the user preference from the input file 'doc.txt' and plays the media/ sends          command to Atmega 8 to open the corresponding shelf
