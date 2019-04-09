# info_697
The programs in this file were exercises for Info 697 at Pratt Institute

odd_even_game.py 
a simple game written for the Micro:bit in Micropython.
tests a child's ability to identify odd or even numbers.

portable_data_logger.py
written for the Micro:bit in Micropython
uses built in compass and temperature sensors to collect direction and temp
every 10 seconds and writes that data to a CSV file stored locally

micro:bit_as_switch.py
written for the Micro:bit in Micropython
uses the write.digital function of the controller to use the Micro:bit as an external 
switch to safely shutdown a Raspberry Pi 3

safe_shutdown_pi.py
written for the Raspberry Pi 3 b+ using Python
Creates a script for safely shutting down a Raspberry Pi by using a Micro:bit
as an external off button
