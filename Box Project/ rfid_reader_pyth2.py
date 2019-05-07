# rfid_reader_pyth2.py
'''This is adapted from code by Tony DiCola, 
(c) 2015 Adafruit Industries, see copyright notice.
Code version is written for Python 2 and requires the 
Adafruit_PN532 library. For directions on cloning the library see: 
https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks/library-installation.
For info on circuitpython, see: https://buildmedia.readthedocs.org/media/pdf/
adafruit-circuitpython-pn532/latest/adafruit-circuitpython-pn532.pdf'''

# Example of detecting and reading a block from a MiFare NFC card.
# Author: Tony DiCola & Roberto Laricchia
# Copyright (c) 2015 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

import binascii
import sys
import time
import RPi.GPIO as GPIO

# enable pin for status LED 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)

# sound_function.py
# see: https://www.pygame.org/docs/ref/mixer.html
# code adapted from https://raspberrypi.stackexchange.com/
# questions/7088/playing-audio-files-with-python
def play_sound_file(file):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

# sound files to play. Future versions will use database 
# if running script from cron, absolute paths to sound files
# are necessary (e.g. /home/pi/Folder/sound_file.wav)        
pomander_info = 'pomander_info.wav'
figurine_info = 'figurine_info.wav'
gregorian_chant = 'music_info.wav'
shut_down_music = 'Shut_down_chant.wav'

# initial sleep time to give pi a chance to boot
time.sleep(2)

# begin setting up reader
import Adafruit_PN532 as PN532

# Python2 configuration for a Raspberry Pi:
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# Create an instance of the PN532 class.
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)

# Call begin to initialize communication with the PN532.  Must be done before
# any other calls to the PN532!
pn532.begin()

# Get the firmware version from the chip and print(it out.)
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

# Main loop to detect cards and play appropriate sound file.
print('Waiting for item...')
while True:
    # turn on LED to indicate that box is active and waiting for scan
    GPIO.output(22, GPIO.HIGH)
    
    # declares known card values as targets. Later versions will rely on a database 
    # rather than if elif check
    pomander = '6c4b1b40'
    figurine = 'a62c04ae'
    chant = 'c5c057c9'
    shut_down = 'a391ca35'
    
    # Check if a card is available to read.
    uid = pn532.read_passive_target()
    # Try again if no card is available.
    if uid is None:
        continue
        
    chip_id = format(binascii.hexlify(uid))
    object = str(chip_id)
    # print(object)
    time.sleep(1)
    
    # conditional loop to play sound files for rfid tags
    if object == pomander:
        print("Found: Pomander")
        print("Playing Sound File")
        play_sound_file(pomander_info)
        time.sleep(2)
    elif object == figurine:
        print("Found: Figurine")
        print("Playing Sound File")
        play_sound_file(figurine_info)
        time.sleep(2)
    elif object == chant:
        print("Found: Chant")
        print("Playing Sound File")
        play_sound_file(gregorian_chant)
        time.sleep(2)
    elif object == shut_down:
        play_sound_file(shut_down_music)
        print("Exiting Program")
        
        # flash LED to indicate that reader is shutting down 
        GPIO.output(22, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(22, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(22, GPIO.LOW)
        break
    else:
        print("Not recognized ... Keep searching")

'''To ensure that this code runs each time the Pi is booted, it is
necessary to run Cron to schedule the script at each reboot. Use the
crontab -e command and use the absolute path to the file using a
command like @reboot python /home/pi/Folder/myscript.py For more information
see: https://www.raspberrypi.org/documentation/linux/usage/cron.md'''