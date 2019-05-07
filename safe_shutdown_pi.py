# safe_shutdown.py

# script to use micro:bit as a safe off switch for the pi

import RPi.GPIO as GPIO
import time
import subprocess

'''Configure pin to receive input on GPIO 21, physical 40.
Physical 40 was chosen because it is next to physical 39, 
which is ground, and because physical 40 and physical 39 are 
at the far end of the header pins making them easier to reach. 
This configuration was recommended for a project using a breadboard
and switch found at: 
https://www.quartoknows.com/page/raspberry-pi-shutdown-button
As this project uses a Micro:Bit for the shut off switch, GPIO.IN 
designates pin 21 as input, setting it to to a low logic level.The 
Micro:Bit is configured to send a +3.3V signal when button b is pushed.
This requires designating pull_down resistors to keep the circuit from
floating. The RPI Labs site (https://rpi.science.uoit.ca/lab/gpio/) 
states that the GPIO.PUD_DOWN command means that "[t]he input is 
considered active if it is receiving +3.3V, inactive otherwise." 
See also: https://grantwinney.com/using-pullup-and-pulldown-
resistors-on-the-raspberry-pi/'''

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# function to shut down pi safely using os to accept the sudo halt command
'''Uses subprocess.run from Python 3 see: 
https://docs.python.org/3.6/library/subprocess.html
According to multiple online sources, this approach avoids potential 
shell-injection attacks. Even though the input is from an electrically 
wired circuit, it is good practice to keep security as firm as possible.'''

def good_night(channel):
    time.sleep(1) 
	print("Shutting Down")
    subprocess.run(['sudo', 'halt'])

# provide initial time for Micro:Bit to be active on boot
time.sleep(5)

# create while loop for pi to scan for input from pin 21
while True:

    '''Use event detection to capture when pin 21 rises in voltage, 
    uses callback to trigger good_night function to shut down pi, and 
    sets a 2 second delay between callbacks. For documentation on this 
    approach, see: http://tieske.github.io/rpi-gpio/modules/GPIO.html
	Placing event detection inside a while True loop causes the 
	event detection to trigger constantly rather than waiting for
	the event. The solution below is from https://stackoverflow.com/
	questions/38125047/raspberry-pi-runtimeerror-conflicting-edge-
	detection-already-enabled-for-this-g'''

	if not 'event' in locals():
		event = GPIO.add_event_detect(21, GPIO.RISING, callback=good_night)
    
# Back up code in case there are problems with event detection.
# This code works just as well.
#     if GPIO.input(21):
# 		good_night()

'''To ensure that this code runs each time the Pi is booted, it is
necessary to run Cron to schedule the script at each reboot. Use the
crontab -e command and use the absolute path to the file using a
command like @reboot python3 /home/pi/Folder/myscript.py For more information
see: https://www.raspberrypi.org/documentation/linux/usage/cron.md'''
