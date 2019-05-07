# Box Project
The scripts here are for the final project for Info 697 at Pratt Institute

Files:

micro:bit_as_switch.py
 Written for the Micro:bit in Micropython
uses the write.digital function of the controller to use the Micro:bit as an external 
switch to safely shutdown a Raspberry Pi 3

safe_shutdown_pi.py
 written for the Raspberry Pi 3 b+ using Python
Creates a script for safely shutting down a Raspberry Pi by using a Micro:bit
as an external off button. Designed to work with a micro:bit flashed with 
micro:bit_as_switch.py

rfid_reader_pyth2.py 
 Written for python 2 to take advantage of the PN532 and SPI libraries developed by 
Adafruit. The library is forked to my repository: 
https://github.com/john-decker/Adafruit_Python_PN532
This code was written for the pi to operate as a headless rfid reader and playback
machine.

Pi_PN532_MB_Python2_Config_bb.jpg
 Fritzing diagram for wiring complete device

Pi_PN532_MB_Python2_Config_small_bb.jpg
 Smaller version of Fritzing diagram for wiring complete device

Hardware:

 Raspberry Pi 3 B+, Micro:Bit, Adafruit PN 532 RFID/NFC Board, USB Speakers, LED


Assembly:

 The project is designed to operate in an enclosed box. The design of the box is flexible but needs: a place for the Micro:Bit in which the B button is accessible, a place for the indicator light, a means of marking where the RFID antenna is, and speakers -- if the speakers are adjustable, access to the adjusment is also necessary. 

Normal Operation:

 The unit only needs to be plugged into wall power. The safe shut down program as well as the RFID reader software on the Pi should be set to boot automatically using cron so that they start once the unit is plugged in. The program on the Micro:Bit should be flashed onto it before it is attached to the Pi so that it is active with power. The indicator light on the front of the box will show whether or not the RFID reader is active. While active, users can place designated items over the RFID reader antenna, which will sense the RFID tags attached to each object. The tags are associated with individual sound files that will play once the reader has recognized a tag. Speakers will output the sound when the appropriate files are played. When it is time to put the objects away and shut down the unit, use the Administrator’s fob.  The Administrator’s fob will exit the RFID reader program at which point a music file will play, the indicator light will blink twice, and then the light will turn off to signal that the RFID reader is no longer active. Finally, the unit can be shut down safely by pressing the B button of the Micro:Bit.  