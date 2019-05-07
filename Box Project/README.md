# Box Project
The scripts here are for the final project for Info 697 at Pratt Institute

micro:bit_as_switch.py
written for the Micro:bit in Micropython
uses the write.digital function of the controller to use the Micro:bit as an external 
switch to safely shutdown a Raspberry Pi 3

safe_shutdown_pi.py
written for the Raspberry Pi 3 b+ using Python
Creates a script for safely shutting down a Raspberry Pi by using a Micro:bit
as an external off button. Designed to work with a micro:bit flashed with 
micro:bit_as_switch.py

rfid_reader_pyth2.py 
written for python 2 to take advantage of the PN532 and SPI libraries developed by 
Adafruit. The library is forked to my repository: 
https://github.com/john-decker/Adafruit_Python_PN532
This code was written for the pi to operate as a headless rfid reader and playback
machine.

Pi_PN532_MB_Python2_Config_bb.jpg
Fritzing diagram for wiring complete device

Pi_PN532_MB_Python2_Config_small_bb.jpg
Smaller version of Fritzing diagram for wiring complete device