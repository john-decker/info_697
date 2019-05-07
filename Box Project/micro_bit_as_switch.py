# simple script to use Micro:Bit as an off switch for a raspberry pi

from microbit import *

# initialize Pin2 in a low logic state

pin2.write_digital(0)

while True:
    if button_a.was_pressed():
        display.scroll("Press B to Shutdown")
        display.clear()

    # use b button to send signal to GPIO pin on raspberry pi
    # signal will trigger shut down script on pi

    if button_b.was_pressed():
        display.scroll("Shutting Down")
        display.clear()
        sleep(1000)
        pin2.write_digital(1)
        sleep(1000)
        pin2.write_digital(0)

