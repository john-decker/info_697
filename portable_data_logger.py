# portable environmental data logger
# collects temperature and compass heading every ten seconds
# stores the information as a csv file on the Micro:Bit

from microbit import *

# function to convert from celsius to farenheit
def centigrade_to_farenheit(number):
    ftemp = ((9/5)*number) + 32
    return ftemp

# function to convert compass heading from degrees to cardinal points
def degrees_to_cardinal(heading):
    if heading == 0:
        return "North"
    elif heading <= 44:
        return "North North East"
    elif heading == 45:
        return "North East"
    elif heading <= 89:
        return "East North East"
    elif heading == 90:
        return "East"
    elif heading <= 134:
        return "East South East"
    elif heading == 135:
        return "South East"
    elif heading <= 180:
        return "South South East"
    elif heading == 180:
        return "South"
    elif heading <= 224:
        return "South South West"
    elif heading == 225:
        return "South West"
    elif heading <= 269:
        return "West South West"
    elif heading == 270:
        return "West"
    elif heading <= 314:
        return "West North West"
    elif heading == 315:
        return "North West"
    elif heading <= 359:
        return "North North West"
    elif heading == 360:
            return "North"

# performs initial check to see if compass is calibrated
if compass.is_calibrated():
    pass
else:
    compass.calibrate()

# initial message to user
display.scroll("Starting Log ...")
sleep(1000)
display.scroll("A for current readings")
display.scroll("B for last readings")

# initialize list
log_file = ["Heading", "Temperature", ]

# begin loop to sample direction and temperature
while True:
    # get readings
    heading = compass.heading()
    ctemp = temperature()
    temp = centigrade_to_farenheit(ctemp)
    
    # convert information to string and append to list
    h_data = str(heading)
    t_data = str(temp)
    log_file.append(h_data)
    log_file.append(t_data)
    
    # write to file
    with open('data_log.csv', 'w') as f_object:
        for item in log_file:
            entry = item + ", "
            f_object.write(entry)

    # put unit to sleep for 10 seconds
    sleep(10000)
    display.scroll("...")
   
    # allow user to see most current heading in degrees and cardinal direction
    # allow user to see most current temp in degrees farenheit
    # allow user to initiate reading by storing current information
    if button_a.was_pressed():
        display.scroll("Current Readings: ")
        display.scroll(heading)
        display.scroll("degrees")
        display.scroll(degrees_to_cardinal(heading))
        display.scroll(temp)
        display.scroll("Farenheit")
        
        # write user-intiated reading to file
        h_data = str(heading)
        t_data = str(temp)
        log_file.append(h_data)
        log_file.append(t_data)
        with open('data_log.csv', 'w') as f_object:
            for item in log_file:
                entry = item + " , "
                f_object.write(entry)
    
    # allow user to see the most recently stored heading and temp data
    if button_b.was_pressed():
        display.scroll("Last Readings: ")
        last_heading = log_file[-2]
        last_temp = log_file[-1]
        display.scroll(last_heading)
        display.scroll("degrees")
        display.scroll(degrees_to_cardinal(heading))
        display.scroll(last_temp)
        display.scroll("Farenheit")